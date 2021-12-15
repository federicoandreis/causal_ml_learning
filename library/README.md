# Library

This folder contains relevant papers in the following folders:
* `ai_robustness`: Use of causal methods to assess / improve the robustness of AI / ML methods.
* `causal_ai`: computational analysis of causal models to identify causal effects
* `causal_inference`: causal inference analysis based on potential outcomes or DAGs
* `conceptual`: key concepts such as exploration / prediction and their link with different methods, opportunities for combining them
* `fairness`: use of causal methods to understand / improve algorithmic fairness
* `heterogeneous treatment effects`: use of machine learning to measure individual factors that explain heterogeneity in intervention impacts
* `mixed_methods`: Interesting combination of methods
* `tools`: documentation for software packages etc.

# Bibliography

Here is a reference list for topics relating the theory and applications of causal inference methods. The applications are mainly in the health research, as that is my background, feel free to add. There might be some duplications.

As a **free** and excellent reference textbook for the main concepts (and more), I definitely suggest 

- Hernán MA and Robins J (2021). Causal Inference - What If. CRC Press [pdf here](https://cdn1.sph.harvard.edu/wp-content/uploads/sites/1268/2021/03/ciwhatif_hernanrobins_30mar21.pdf).

You can also find a [repo](https://github.com/jrfiedler/causal_inference_python_code) with a Python code companion for the book. Datasets used, and SAS, Stata and R code can also be found on the [book page](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/), together with a few more resources.


**Theory of causal inference**

- Hernán MA and Robins J (2021). Causal Inference - What If. CRC Press [url](https://cdn1.sph.harvard.edu/wp-content/uploads/sites/1268/2021/03/ciwhatif_hernanrobins_30mar21.pdf), [book page](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/).

- Hernán MA, Hernández-Díaz S, Werler MM and Mitchell AA (2002). Causal Knowledge as a Prerequisite for Confounding Evaluation: An Application to Birth Defects Epidemiology. American Journal of Epidemiology 155 (2): 176–84 [url](https://doi.org/10.1093/aje/155.2.176).

- Hèrnan MA (2017). Causal Diagrams: Draw Your Assumptions Before Your Conclusions. [url](https://www.edx.org/course/causal-diagrams-draw-assumptions-harvardx-ph559x).

- Hèrnan MA,Clayton D and Keiding N (2011). The Simpon’s paradox unraveled. International Journal of Epidemiology 40 (3): 780–85.

- Munafò MR, Tilling K, Taylor AE, Evans DM and Smith GD (2018). Collider Scope: When Selection Bias Can Substantially Influence Observed Associations. International Journal of Epidemiology 47 (1):226–35 [url](https://doi.org/10.1093/ije/dyx206).

- Murray E (2018). What Is a Cause? [url](https://medium.com/@EpiEllie/what-is-a-cause-da8c5522ccde).

- Neuhaus JM and Jewell NP (1993). A Geometric Approach to Assess Bias Due to Omitted Covariates in Generalized Linear Models. Biometrika 80 (4): 807–15.

- Pearl J (2018). The Book of Why: The New Science of Cause and Effect. New York, US: Allen Lane.

- Pearl J, Glymour M and Jewell NP (2016). Causal Inference in Statistics: A Primer. Chichester, UK: Wiley.

- Pearl J (1995). Causal Diagrams for Empirical Research. Biometrika 82 (4): 669–88 [url](http://www.jstor.org/stable/2337329).

- Rubin DB (2005). Causal Inference Using Potential Outcomes. Journal of the American Statistical Association, 100(469): 322–31 [url](https://doi.org/10.1198/016214504000001880).

**Propensity Scores**

- Austin PC (2009). Balance Diagnostics for Comparing the Distribution of Baseline Covariates between Treatment Groups in Propensity-Score Matched Samples. Statistics in Medicine, 28:3083–-107.

- Austin PC (2011). An Introduction to Propensity Score Methods for Reducing the Effects of Confounding in Observational Studies. Multivariate Behav Res, 46(3):399--424. doi:10.1080/00273171.2011.568786.

- Dehejia RH and Wahba S (1999), Causal Effects in Non-Experimental Studies: Re-Evaluating the Evaluation of Training Programs. Journal of the American Statistical Association 94(448):1053--1062.

- Garrido MM, Kelley AS, Paris J, et al (2014). Methods for constructing and assessing propensity scores. Health Serv Res, 49(5):1701--1720. doi:10.1111/1475-6773.12182.

- Hernán MA and Robins J (2021). Causal Inference - What If. CRC Press [url](https://cdn1.sph.harvard.edu/wp-content/uploads/sites/1268/2021/03/ciwhatif_hernanrobins_30mar21.pdf), [book page](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/).

- Ho DE, Imai K, King G and Stuart EA (2011). MatchIt: Nonparametric Preprocessing for Parametric Causal Inference. Journal of Statistical Software, 42(8), 1–28. https://www.jstatsoft.org/v42/i08/.

- Imai K and Ratkovic M (2014). Covariate balancing propensity scores. J R Stat Soc B, 76(1):243--263.

- Rosenbaum PR and Rubin DB (1983). The Central Role of the Propensity Score in Observational Studies for Causal Effects. Biometrika, 70(1):41--55.

- Rosenbaum PR and Rubin DB (1985). Constructing a Control Group using Multivariate Matched Sampling Methods That Incorporate the Propensity Score. The American Statistician 39 (1):33–-8.

**Mediation Analysis**

- Baron, R. M., & Kenny, D. A. (1986). The moderator mediator variable distinction in social psychological research: Conceptual, strategic, and statistical considerations. Journal of personality and social psychology, 51(6), 1173.

- Bellavia, A., Bottai, M., Orsini, N. (2016). Evaluating Additive Interaction Using Survival Percentiles. Epidemiology, 27(3), 360.

- Bellavia A, Williams PL, Dimeglio LA, Hazra R, Abzug MJ, Patel K, Jacobson DL, Van Dyke RB, Geffner ME. (2017) Delay in sexual maturation in perinatally HIV-infected youth is mediated by poor growth. AIDS.

- Bind, M. A., Vanderweele, T. J., Coull, B. A., & Schwartz, J. D. (2016). Causal mediation analysis for longitudinal data with exogenous exposure. Biostatistics, 17(1), 122-134.

- Fulchner, E., Tchetgen Tchetgen, E., and Williams, P. (2017). Mediation Analysis for Censored Survival Data under an Accelerated Failure Time Model. Epidemiology Gamborg, M., 

- Jensen, G. B., Srensen, T. I., & Andersen, P. K. (2011). Dynamic path analysis in life-course epidemiology. American journal of epidemiology, 173(10), 1131-1139.

- Hernandez-Diaz S, Schisterman EF, Hernn MA. (2006) The birth weight paradox uncovered?. American journal of epidemiology. 1;164(11):1115-20.

- Imai, K., Keele, L., & Tingley, D. (2010). A general approach to causal mediation analysis. Psychological methods, 15(4), 309.

- Imai, K., Keele, L., Tingley, D., Yamamoto, T. (2010). Causal mediation analysis using R. In: H.D. Vinod (ed.), Advances in Social Science Research Using R. New York: Springer
(Lecture Notes in Statistics), p.129-154.

- Lange, T., & Hansen, J. V. (2011). Direct and indirect effects in a survival context. Epidemiology, 22(4), 575-581.

- Li, R., & Chambless, L. (2007). Test for additive interaction in proportional hazards models. Annals of epidemiology, 17(3), 227-236.

- Pearl, J. (2001). Direct and indirect effects. In Proceedings of the seventeenth conference on uncertainty in artificial intelligence (pp. 411-420). Morgan Kaufmann Publishers Inc.

- Robins, J. M., & Greenland, S. (1992). Identifiability and exchangeability for direct and indirect effects. Epidemiology, 143-155.

- Rod, N. H., Lange, T., Andersen, I., Marott, J. L., & Diderichsen, F. (2012). Additive interaction in survival analysis: use of the additive hazards model. Epidemiology, 23(5), 733-737.

- Rothman KJ. (1976). Causes. Am J of Epidemiol 104:587-592.

- Strohmaier, S., Rysland, K., Hoff, R., Borgan, ., Pedersen, T. R., & Aalen, O. O. (2015).

- Dynamic path analysisa useful tool to investigate mediation processes in clinical survival trials. Statistics in medicine, 34(29), 3866-3887.

- Tein, J. Y., & MacKinnon, D. P. (2003). Estimating mediated effects with survival data. In New developments in psychometrics (pp. 405-412). Springer Japan.

- VanderWeele, T. J. (2011). Causal mediation analysis with survival data. Epidemiology (Cambridge, Mass.), 22(4), 582.

- VanderWeele, T.J. (2015). Explanation in causal inference: methods for mediation and interaction. Oxford University Press.

- VanderWeele, T. J. (2009). On the distinction between interaction and effect modification. Epidemiology, 20(6), 863-871.

- VanderWeele, T.J., & Vansteelandt, S. (2013). Mediation analysis with multiple mediators. Epidemiologic methods, 2(1), 95-115.

- VanderWeele, T.J. and Vansteelandt, S. (2010). Odds ratios for mediation analysis with a dichotomous outcome. American Journal of Epidemiology, 172:1339-1348.

- VanderWeele, T. J. (2009). Marginal structural models for the estimation of direct and indirect effects. Epidemiology, 20(1), 18-26.

- VanderWeele, T. J. (2014). A unification of mediation and interaction: a 4-way decomposition. Epidemiology, 25(5), 749-761.

- VanderWeele, T.J. and Knol, M.J. (2014). A tutorial on interaction. Epidemiologic Methods.

- Valeri, L., & VanderWeele, T. J. (2013). Mediation analysis allowing for exposuremediator interactions and causal interpretation: Theoretical assumptions and implementation with SAS and SPSS macros. Psychological methods, 18(2), 137.
