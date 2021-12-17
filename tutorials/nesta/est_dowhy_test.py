## Firebreak week December 2021 - Causal Inference & Machine Learning
#
# Short tutorial for the DoWhy package (https://microsoft.github.io/dowhy/)
#
# This tutorial makes use of a pre-processed subset of the EST data (np_processed.csv),
# that contains a number of variables. The ones relevant for this example are the
# following aggregates at the postcode level:
#
# n_heat_pump (outcome variable)
# median_property_age ("treatment" variable)
# n_household
# median_floor_area
# median_epc_score
# median_energy_consumption
# median_co2_emissions
# median_low_energy_lighting.
#
# Underlying theory and data-driven considerations suggest a tentative structure for
# causality linking the above variables, which is encoded in a graph object in STEP 1.
# The causal structure can be specified using GML (Graph Modelling Language, here used) or DOT. It is
# also possible to obtain a .png image of the associated DAG.
# Please note that the causal model is tentative and certainly leaves out relevant factors, so take it 
# for what it is: an excuse to learn how to use the package!
#
# STEP 2 concerns identifiability of the desired causal effect (ATE, ATT, ATC), which uses graph-theoretical 
# results to assess the chain of conditional independencies implied by the DAG defined in STEP 1, 
# via multiple criteria (back-door, front-door, instrumental variables, ...). Other approaches are
# possible, for example if a mediation analysis is of interest, but not explored here.
#
# STEP 3 is about estimation of the identifiable causal effect(s). One of the simplest methods makes use of
# a simple linear regression that adjusts for propensity scores, which is demonstrated below. As this might not
# be reasonable/desirable, the package supports alternative estimation methods. On top of that, there seems to
# be support for the wider class of Generalised Linear Models, via the statsmodels module; here I exemplify
# this by fitting a Poisson regression with canonical (log) link to the outcome to perform the causal estimation task.
# Support for more algorithmic approaches is also present: DoWhy allows functions from EconML (https://github.com/microsoft/EconML)
# and CausalML (https://github.com/uber/causalml), which allow for estimation of conditional causal effects (CATE),
# to be used (not explored here).
#
# STEP 4 concerns sensitivity analysis. DoWhy implements a number of sense-checks (some in the form of statistical tests) 
# to asses the robustness of the combination data/hypothesised causal structure.

# imports
import dowhy
import pandas as pd
import pygraphviz
import numpy as np
import os
from pathlib import Path

# read in data
keep_variables = ["n_heat_pumps","n_households","median_floor_area","median_property_age","median_epc_score",
"median_energy_consumption", "median_co2_emissions", "median_low_energy_lighting"]

PROJECT_DIR = Path(__file__).resolve().parents[2]

dataset = pd.read_csv(str(PROJECT_DIR)+"/data/est_processed.csv")

# pre- and post-processing
# data already pre-processed (in R) for simplicity, just a few tweaks needed

# dichotomise treatment
dataset['median_older_than_1950'] = np.where(dataset.loc[:,["median_property_age"]] < 4, True, False)


## STEP 1: THE CAUSAL MODEL
# define a simple causal model


causal_graph = """digraph {
median_older_than_1950[label="Older Than 1950"];
n_households[label="Number of Households"];
n_heat_pumps[label="Number of Installations"];
median_floor_area[label="Floor Area"];
median_epc_score[label="EPC score"];
median_co2_emissions[label="CO2 Emissions"];
median_low_energy_lighting[label="Low Energy Lighting"];
median_energy_consumption[label="Energy Consumption"];
U[label="Unobserved Confounders"];
U -> {median_older_than_1950, n_heat_pumps};
n_households -> n_heat_pumps;
median_older_than_1950 -> {median_epc_score, n_heat_pumps, median_energy_consumption};
median_energy_consumption -> median_co2_emissions;
median_low_energy_lighting -> {median_energy_consumption, median_co2_emissions};
median_floor_area -> median_epc_score;
median_epc_score -> n_heat_pumps;
n_heat_pumps -> median_co2_emissions
}"""


# visualise DAG
model= dowhy.CausalModel(
        data = dataset,
        graph=causal_graph.replace("\n", " "),
        treatment='median_older_than_1950',
        outcome='n_heat_pumps')

model.view_model() # this returns a .png

## STEP 2: IDENTIFICATION

import statsmodels.api as sm

identified_estimand = model.identify_effect(proceed_when_unidentifiable=True)
print(identified_estimand)

## STEP 3: ESTIMATION
# estimate the causal effect
# ATE = Average Treatment Effect
# ATT = Average Treatment Effect on Treated (i.e. those households older than 1950s)
# ATC = Average Treatment Effect on Control (i.e. those households younger than 1950s)

estimate = model.estimate_effect(identified_estimand,method_name="backdoor.propensity_score_stratification",target_units="ate")

print(estimate)

# try different models
estimate_glm = model.estimate_effect(identified_estimand,method_name="backdoor.generalized_linear_model",target_units="ate",
confidence_intervals=True,test_significance=False,method_params = {
    'num_null_simulations':10,
    'num_simulations':10,
    'num_quantiles_to_discretize_cont_cols':10,
    'fit_method': "statsmodels",
    'glm_family': sm.families.Poisson(), # Poisson regression - wonder if I can put something more complex here...
#    'exposure': dataset.n_households, # this does not seem to work :/
    'need_conditional_estimates':False
    })
print(estimate_glm)
print(estimate_glm.estimator.model.summary())
estimate_glm.interpret()

# # with EconML
# import econml # package is installed, but not found...
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LassoCV
# from sklearn.ensemble import GradientBoostingRegressor
# dml_estimate = model.estimate_effect(identified_estimand, method_name="backdoor.econml.dml.DML",
#                                      control_value = 0,
#                                      treatment_value = 1,
#                                  target_units = lambda df: df["median_co2_emissions"]>150,  # condition used for CATE
#                                  confidence_intervals=True,
#                                 method_params={"init_params":{'model_y':GradientBoostingRegressor(),
#                                                               'model_t': GradientBoostingRegressor(),
#                                                               "model_final":LassoCV(fit_intercept=False), 
#                                                               'featurizer':PolynomialFeatures(degree=1, include_bias=False)},
#                                                "fit_params":{}})
# print(dml_estimate)


## STEP 4: SENSITIVITY ANALYSIS

# 1. random common cause --- estimate should not change much
refute1_results=model.refute_estimate(identified_estimand, estimate,method_name="random_common_cause")
print(refute1_results)

# 2. placebo treatment refuter --- estimate should go to zero
refute2_results=model.refute_estimate(identified_estimand, estimate,method_name="placebo_treatment_refuter")
print(refute2_results)

# 3. Data Subset Refuter --- estimate should not change much
refute3_results=model.refute_estimate(identified_estimand, estimate,method_name="random_common_cause")
print(refute3_results)
