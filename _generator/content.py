# -*- coding: utf-8 -*-
# =============================================================================
#  ALL THE WORDS ON YOUR WEBSITE LIVE IN THIS FILE.
#
#  Edit it on github.com (pencil icon), commit, wait about a minute. The site
#  rebuilds itself. Never edit the .html files -- they are regenerated from
#  this one and your changes there would be wiped out.
#
#  Three rules that cover almost every mistake:
#    1. Text goes inside "quotes". Keep both of them.
#    2. Every line in a list ends with a comma.
#    3. Use &rsquo; for an apostrophe and &mdash; for a long dash, so they
#       display correctly in a browser.
#
#  If you break something the website does NOT break -- the rebuild just fails
#  and the old pages stay up. Check the Actions tab for a red cross.
#
#  WHAT TO EDIT, AND WHERE (search for the word in capitals):
#    ROLE, TAG, EMAIL ...... your title, one-line summary, contact
#    BIO ................... the About page paragraphs
#    NEWS .................. the news list on the homepage
#    AREAS ................. the three research sections
#    METHODS + SLUGS ....... your publications
#    PEOPLE ................ the People page
#    COURSES ............... the Teaching page
# =============================================================================
NAME  = "Aaron Wolfe Scheffler"
ROLE  = "Associate Professor"
ROLE_FULL = "Associate Professor in Residence"
DEPT  = "Department of Epidemiology &amp; Biostatistics"
INST  = "University of California, San Francisco"
EMAIL = "aaron.scheffler@ucsf.edu"
CV    = "../shared/aaron_cv_2026.pdf"
TAG   = "Statistical methods for highly structured biomedical data &mdash; disease progression models, multimodal neuroimaging, and functional data analysis."
SHORT = "Associate Professor of Epidemiology & Biostatistics at UCSF. Statistical methods for structured biomedical data."

LINKS = [("CV", CV),
         ("Google Scholar","https://scholar.google.com/citations?user=4aba0JUAAAAJ&hl=en"),
         ("GitHub","https://github.com/aaron-scheffler"),
         ("UCSF Profile","https://profiles.ucsf.edu/aaron.scheffler"),
         ("Email","mailto:aaron.scheffler@ucsf.edu")]

NAV = [("index.html","About"),("research.html","Research"),
       ("publications.html","Publications"),("people.html","People"),("teaching.html","Teaching")]

# --- BIO: the paragraphs on your About page ------------------------------
# One paragraph per pair of quotes. <strong>bold</strong> and
# <a href="...">links</a> both work.
BIO = [
 'I am an Associate Professor in Residence in the <a href="https://profiles.ucsf.edu/aaron.scheffler">Department of Epidemiology &amp; Biostatistics</a> at the University of California, San Francisco. My research program addresses the statistical challenges that arise in highly structured biomedical data &mdash; disease progression models, joint models of multi-modal brain images, high-dimensional regressions, functional data analysis, and curve registration and warping.',
 'I am a core statistician for several centers at the UCSF Memory and Aging Center, including the Alzheimer’s Disease Research Center and the <a href="https://websites.ucsf.edu/website/alba-language-neurobiology-lab">ALBA Language Neurobiology Laboratory</a>, and I hold faculty affiliations in Computational Precision Health, the Bakar Computational Health Sciences Institute, and the Center for Intelligent Imaging. I maintain a wide set of collaborations with clinical and public health researchers at UCSF in neurology, orthopedics, and HIV/AIDS.',
 'My methodological research is supported by an <strong>NIH/NINDS R01</strong> on Bayesian object-oriented modeling of multi-modal imaging data, and I serve as a Multiple Principal Investigator and Associate Program Director for Biostatistics and AI on the <strong>UCSF CTSA K12</strong> program.',
 'Prior to UCSF I received a doctorate from the Department of Biostatistics at UCLA under the advisement of <a href="https://ph.ucla.edu/about/faculty-staff-directory/damla-senturk">Dr. Damla Senturk</a>, and a BA in Biochemistry from Columbia University.',
]

# --- NEWS: the list on your homepage -------------------------------------
# Newest at the top. Each line is:
#     ("Date", "kind", "The sentence", flag),
# kind must be one of: paper  funding  position  other   (sets the little label)
# flag is None, or "Filled" for a job advert that has been filled.
# To add an item, copy a whole line, paste it above, and change the wording.
NEWS = [
 # (date, kind, html, flag)   kind: position | funding | paper | other
 ("July 2026","other","I have been promoted to <strong>Associate Professor in Residence</strong> in the Department of Epidemiology &amp; Biostatistics at UCSF.",None),
 ('July 2026','funding','We&rsquo;re funded! I am part of <strong>Team ATLAS</strong>, awarded a <strong>Dementia Frontiers Fund</strong> grant from Alzheimer&rsquo;s Research UK and Gates Ventures. The team is led by Professor Duygu Tosun (University of California, San Francisco) and Dr Oliver Robinson (Imperial College London), and brings together researchers from the US, UK and Spain to study the amyloid-to-tau interval and the factors that accelerate or delay the onset of symptoms. More information can be found <a href="https://www.alzheimersresearchuk.org/news/dementia-frontiers-fund-backs-12-international-teams/">here</a>.',None),
 ("July 2026","funding","We&rsquo;re funded! We were awarded an <strong>NIH/NCATS K12</strong> grant titled &ldquo;CTSA K12 Program at UCSF.&rdquo; I serve as a Multiple Principal Investigator and Associate Program Director for Biostatistics and AI.",None),
 ("January 2026","position","We&rsquo;re hiring! Dr. Rajarshi Guhaniyogi and I are seeking a postdoctoral research associate for an NIH-funded research program, beginning September 2026. The research relates to one or more of the following areas: Bayesian learning with heterogeneous objects (e.g.&nbsp;tensor and functional data); Bayesian interpretable deep learning with heterogeneous objects; distributed Bayesian computation and federated learning with Gaussian processes and their variants; and data sketching with random sketching matrices for efficient Bayesian inference with massive structured data. Please e-mail me directly for more information.","Filled"),
 ("2025","paper","Our paper &ldquo;Sketching in high-dimensional regression with big data using Gaussian scale mixture priors&rdquo; is published in the <em>Journal of Machine Learning Research</em>. This is joint work with <a href=\"https://sites.google.com/view/rajguhaniyogi/home\">Dr. Rajarshi Guhaniyogi</a>.",None),
 ("2025","paper","Our paper &ldquo;Multi-object data integration in the study of primary progressive aphasia&rdquo; is published in <em>The Annals of Applied Statistics</em>.",None),
 ("April 2024","funding","We&rsquo;re funded! I am a Co-Investigator on an <strong>NIH/NIA P30</strong> grant titled &ldquo;New Approaches to Dementia Heterogeneity&rdquo; (PI: Rabinovici).",None),
 ("2024","paper","Our paper &ldquo;A Bayesian covariance based clustering for high-dimensional tensors&rdquo; is accepted in <em>Technometrics</em>.",None),
 ("January 2024","position","We&rsquo;re hiring! Dr. Rajarshi Guhaniyogi and I are seeking a postdoctoral research associate for an NIH-funded research program at the Department of Statistics, Texas A&amp;M University, starting as early as May 2024. The research relates to one or more of the following areas: Bayesian learning with heterogeneous objects (e.g.&nbsp;tensor and functional data); Bayesian interpretable deep learning with heterogeneous objects; distributed Bayesian computation and federated learning with Gaussian processes and their variants; and data sketching with random sketching matrices for efficient Bayesian inference with massive structured data. Please e-mail me directly for more information.","Filled"),
 ("August 2023","funding","We&rsquo;re funded! I am a Co-Investigator on an <strong>NIH/NIA P01</strong> grant titled &ldquo;Frontotemporal Dementia: Genes, Images, and Emotions&rdquo; (PI: Gorno-Tempini).",None),
 ("June 2023","funding","We&rsquo;re funded! I am a Co-Investigator on an <strong>NIH/NIAMS R01</strong> grant titled &ldquo;Mechanistic Structure-Function Relationships for Paraspinal Muscle Fat Infiltration in Chronic Low Back Pain Patients&rdquo; (PI: Bailey).",None),
 ("April 2023","funding","We&rsquo;re funded! I was awarded an <strong>NIH/NINDS R01</strong> grant titled &ldquo;Bayesian Object-Oriented Modeling of Multi-Modal Imaging Data.&rdquo; This is joint work with <a href=\"https://sites.google.com/view/rajguhaniyogi/home\">Dr. Rajarshi Guhaniyogi</a>.",None),
 ("2023","paper","Our paper &ldquo;Bayesian adaptive design for covariate-adaptive historical control information borrowing&rdquo; is published in <em>Statistics in Medicine</em>.",None),
 ("2023","paper","Our book chapter &ldquo;Modeling longitudinal trends in event-related potentials&rdquo; is published.",None),
 ("June 2022","funding","We&rsquo;re funded! I was awarded an <strong>NSF DMS</strong> grant titled &ldquo;Use of Random Compression Matrices for Scalable Inference in High Dimensional Structured Regressions.&rdquo; The full project description can be found <a href=\"https://www.nsf.gov/awardsearch/showAward?AWD_ID=2210206\">here</a>.",None),
 ("2022","paper","Our paper &ldquo;Multilevel hybrid principal components analysis for region-referenced functional electroencephalography data&rdquo; is published in <em>Statistics in Medicine</em>.",None),
 ("2022","paper","Our paper &ldquo;Covariate-adjusted hybrid principal components analysis for region-referenced functional EEG data&rdquo; is published in <em>Statistics and its Interface</em>.",None),
 ("2020","paper","Our paper &ldquo;Hybrid principal components analysis for region-referenced longitudinal functional EEG data&rdquo; is published in <em>Biostatistics</em>.",None),
 ("2019","paper","Our paper &ldquo;Covariate-adjusted region-referenced generalized functional linear model for EEG data&rdquo; is published in <em>Statistics in Medicine</em>.",None),
 ("2017","paper","Our paper &ldquo;A multi-dimensional functional principal components analysis of EEG data&rdquo; is published in <em>Biometrics</em>.",None),
]
NEWS_LINK = {
 "Bayesian adaptive design":"https://pubmed.ncbi.nlm.nih.gov/37750361/",
 "Sketching in high-dimensional":"https://arxiv.org/abs/2105.04795",
 "Multi-object data integration":"https://arxiv.org/abs/2407.09542",
 "Multilevel hybrid principal":"https://pubmed.ncbi.nlm.nih.gov/35611602/",
 "Covariate-adjusted hybrid principal":"https://pubmed.ncbi.nlm.nih.gov/35664510/",
 "Hybrid principal components analysis for region-referenced longitudinal":"https://pubmed.ncbi.nlm.nih.gov/30084925/",
 "Covariate-adjusted region-referenced generalized":"https://pubmed.ncbi.nlm.nih.gov/31659786/",
 "A multi-dimensional functional principal":"https://pubmed.ncbi.nlm.nih.gov/28072468/",
}
NEWS_KIND = {"position":"Position","funding":"Funding","paper":"Publication","other":"Announcement"}

RESEARCH_INTRO = 'My research centers on the statistical challenges posed by highly structured data collected in an increasing number of applications, from imaging to wearable technologies. Frequently the observed data are discrete samples of an underlying functional process with complex dependencies that traditional models cannot capture. A central theme is providing computationally efficient methods for these rich data structures that preserve information along each dimension while producing interpretable components and inferences.'

# --- AREAS: the three sections of the Research page -----------------------
#   t     = the heading
#   body  = the paragraphs, one per pair of quotes
#   tags  = the small labels underneath
#   pubs  = which papers are listed at the bottom, using the short names in SLUGS
AREAS = [
 dict(id="dpm", n="01", t="Disease progression models",
   img="tadpole.png", ratio="580/350",
   alt="Estimated biomarker trajectories aligned along a latent disease-time axis.",
   cap="Biomarker trajectories aligned on a latent disease-time axis, allowing subject-level variation in onset, rate, and amplitude to be estimated separately.",
   body=['Disease progression models (DPMs) are critical tools for characterizing the etiology of neurodegenerative disorders and capturing treatment effects in prospective clinical trials. Their development is complicated by subject-level variability in age of onset, rate of progression, and signal amplitude.',
         'We develop Bayesian DPMs that model progression across heterogeneous biomarkers by explicitly modeling subject-specific variation in phase, amplitude, and rate. These produce inference on the timing and ordering of biomarkers and partition that variation between subject-level risk factors and individual variation. Current work explores threshold-aligned joint models for Alzheimer’s disease, extensions to time-to-event modeling, and the computational challenges of high-dimensional multi-modal imaging.'],
   tags=["Bayesian nonlinear mixed models","Curve alignment","Time-to-event","Forecasting"],
   pubs=["dpm-align"]),
 dict(id="imaging", n="02", t="Multi-modal brain imaging",
   img="multimodal.png", ratio="580/232",
   alt="Schematic linking structural and network brain imaging modalities through a joint prior.",
   cap="Structural and network-valued images linked through a joint prior, allowing information to be shared across modalities.",
   body=['Neurodegenerative disorders cause cognitive decline by disrupting structure and connectivity in healthy brains, changes detectable only across multiple imaging modalities. Images carry either structural or network information, and must be linked through joint models to support principled clinical inference. Few statistical models integrate both, because the multimodal structure combines high-dimensional signals, complex correlations, and heterogeneous data types.',
         'This gap does more than limit interpretation: it biases estimated effects, reduces efficiency, and increases sensitivity to noise. We develop Bayesian frameworks that treat multiple brain images as multi-objects, exploiting object topology while leveraging linkages among objects to perform inference, clustering, and prediction, alongside deep generative and explainable-AI approaches to spatial and network images. This work is motivated by imaging studies in primary progressive aphasia at the <a href="https://websites.ucsf.edu/website/alba-language-neurobiology-lab">ALBA Language Neurobiology Laboratory</a>.'],
   tags=["Hierarchical Bayes","Tensor methods","Object-oriented data","Explainable AI"],
   pubs=["multiobj","tensorclust","inva","xai","geostat","sketching"]),
 dict(id="fda", n="03", t="Functional data analysis of EEG",
   img="hpca.png", ratio="580/350",
   alt="Hybrid principal component decomposition of region-referenced functional EEG data.",
   cap="Hybrid principal components decomposition of region-referenced EEG, separating variation along frequency, region, and subject dimensions.",
   body=['Functional data analysis offers a powerful framework that embraces the underlying structure of these data by assuming the basic unit of observation is a signal observed over a continuous domain. This lets us model variation along frequency, spatial region, and time simultaneously rather than collapsing each dimension to a scalar summary.',
         'This research is motivated by electroencephalography studies in children with autism spectrum disorder conducted with collaborators at <a href="http://jestelab.org/">The Jeste Developmental Neurophysiology Lab</a> and the <a href="https://medicine.yale.edu/ycci/programsprojects/autism/">Autism Biomarker Consortium for Clinical Trials</a>.'],
   tags=["Functional PCA","Curve registration","EEG biomarkers"],
   pubs=["multilevel-hpca","cov-hpca","hpca","gflm","mdfpca","erp-chapter","surrogates"]),
]

ME = '<b class="me">Scheffler AW</b>'

# (year, title, authors, venue, detail, url, role)
# --- METHODS: your publications ------------------------------------------
# Newest first. Each entry is:
#     (year, "Title", "Authors", "Journal", "volume/pages", "link or None", "ROLE"),
# Use "Preprint" as the journal for anything not yet published -- that is what
# sends it to the "Working papers" section.
# {ME} inside the authors prints your own name in bold. Leave it as is.
# IMPORTANT: after adding an entry here, add a short nickname in SLUGS below,
# in the SAME position (first entry here = first nickname there).
METHODS = [
 (2026,"Uncertainty-aware neural multivariate geostatistics",
  f"Jeon Y, {ME}, Guhaniyogi R","Preprint","arXiv:2602.16146","https://arxiv.org/abs/2602.16146","CO"),
 (2026,"Bayesian threshold-aligned joint disease progression modeling for Alzheimer’s disease",
  f"Wu R, Tosun D, Hausle I, Heston M, {ME}","Preprint","arXiv:2606.18139","https://arxiv.org/abs/2606.18139","SENIOR"),
 (2025,"Sketching in high-dimensional regression with big data using Gaussian scale mixture priors",
  f"Guhaniyogi R, {ME}","Journal of Machine Learning Research","26(271), 1&ndash;28","https://arxiv.org/abs/2105.04795","SENIOR"),
 (2025,"Multi-object data integration in the study of primary progressive aphasia",
  f"Gutierrez R, {ME}, Guhaniyogi R, Gorno-Tempini ML, Mandelli ML, Battistella G",
  "The Annals of Applied Statistics","19(4), 3282","https://arxiv.org/abs/2407.09542","CO"),
 (2025,"Deep generative modeling with spatial and network images: an explainable AI (XAI) approach",
  f"Jeon Y, Guhaniyogi R, {ME}","Preprint","arXiv:2505.12743","https://arxiv.org/abs/2505.12743","SENIOR"),
 (2025,"Interpretable deep neural network for modeling functional surrogates",
  f"Jeon Y, Guhaniyogi R, {ME}, Francom D, Pasqualini D","Preprint","arXiv:2503.20528","https://arxiv.org/abs/2503.20528","CO"),
 (2024,"A Bayesian covariance based clustering for high-dimensional tensors",
  f"Gutierrez R, {ME}, Guhaniyogi R","Technometrics","Accepted",None,"CO"),
 (2024,"INVA: Integrative variational autoencoder for harmonization of multi-modal neuroimaging data",
  f"Lei B, Guhaniyogi R, Chandra K, {ME}, Mallick B","Preprint","arXiv:2402.02734","https://arxiv.org/abs/2402.02734","CO"),
 (2023,"Bayesian adaptive design for covariate-adaptive historical control information borrowing",
  f"Jin H, Kim M-O, {ME}, Jiang F","Statistics in Medicine","42(29), 5338&ndash;5352","https://pubmed.ncbi.nlm.nih.gov/37750361/","CO"),
 (2023,"Modeling longitudinal trends in event-related potentials",
  f"Şentürk D, {ME}","Book chapter",None,None,"SENIOR"),
 (2022,"Multilevel hybrid principal components analysis for region-referenced functional electroencephalography data",
  f"Campos E, {ME}, Telesca D, Sugar CA, DiStefano C, Jeste S, Levin AR, Naples A, Webb SJ, Shic F, et al.",
  "Statistics in Medicine","41(19), 3737&ndash;3757","https://pubmed.ncbi.nlm.nih.gov/35611602/","CO"),
 (2022,"Covariate-adjusted hybrid principal components analysis for region-referenced functional EEG data",
  f"{ME}, Dickinson A, DiStefano C, Jeste S, Şentürk D","Statistics and Its Interface","15(2), 209",
  "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9165697/pdf/nihms-1759541.pdf","FIRST"),
 (2020,"Hybrid principal components analysis for region-referenced longitudinal functional EEG data",
  f"{ME}, Telesca D, Li Q, Sugar CA, DiStefano C, Jeste S, Şentürk D","Biostatistics","21(1), 139&ndash;157","https://pubmed.ncbi.nlm.nih.gov/30084925/","FIRST"),
 (2019,"Covariate-adjusted region-referenced generalized functional linear model for EEG data",
  f"{ME}, Telesca D, Sugar CA, Jeste S, Dickinson A, DiStefano C, Şentürk D","Statistics in Medicine","38(30), 5587&ndash;5602","https://pubmed.ncbi.nlm.nih.gov/31659786/","FIRST"),
 (2017,"A multi-dimensional functional principal components analysis of EEG data",
  f"{ME}, Hasenstab K, Telesca D, Sugar CA, Jeste S, DiStefano C, Şentürk D","Biometrics","73(3), 999&ndash;1009","https://pubmed.ncbi.nlm.nih.gov/28072468/","FIRST"),
]

# --- SLUGS: a short nickname for each paper above, in the SAME ORDER ------
# Used by AREAS to decide which papers appear on the Research page.
# Add one here whenever you add one to METHODS.
SLUGS = [
 "geostat",         # Uncertainty-aware neural multivariate geostatistics
 "dpm-align",       # Bayesian threshold-aligned joint disease progression
 "sketching",       # Sketching in high-dimensional regression
 "multiobj",        # Multi-object data integration in PPA
 "xai",             # Deep generative modeling, XAI
 "surrogates",      # Interpretable DNN for functional surrogates
 "tensorclust",     # Bayesian covariance based clustering
 "inva",            # INVA harmonization
 "adaptive",        # Bayesian adaptive design
 "erp-chapter",     # Modeling longitudinal trends in ERPs
 "multilevel-hpca", # Multilevel hybrid PCA
 "cov-hpca",        # Covariate-adjusted hybrid PCA
 "hpca",            # Hybrid PCA, Biostatistics
 "gflm",            # Covariate-adjusted region-referenced GFLM
 "mdfpca",          # Multi-dimensional FPCA, Biometrics
]
M = {k: v for k, v in zip(SLUGS, METHODS)}

ROLE_LABEL = {"FIRST":"First author","SENIOR":"Senior author","CO":"Co-author","SOLE":"Sole author"}
ROLE_ORDER = ["FIRST","SENIOR","CO","SOLE"]

PUB_INTRO = ('Below are my <strong>methodological</strong> publications, grouped by year, with my author position '
             'marked on each. Collaborative clinical and public-health papers &mdash; where I contribute statistical '
             'expertise to a larger study team &mdash; are listed separately in my '
             f'<a href="{CV}">CV</a>.')
PUB_NOTE = ('The 2017 <em>Biometrics</em> paper received the Best Student Paper award from the Western North American '
            'Region of the International Biometric Society (2016). A complete list of all publications, including '
            'more than sixty collaborative papers, is available in my '
            f'<a href="{CV}">CV</a> and on '
            '<a href="https://scholar.google.com/citations?user=4aba0JUAAAAJ&hl=en">Google Scholar</a>.')

SOFTWARE = [
 ("HPCA","R","Hybrid principal components analysis for region-referenced functional EEG data.","https://github.com/aaron-scheffler/HPCA"),
 ("MD-FPCA","MATLAB","Multi-dimensional functional principal components analysis.","https://github.com/aaron-scheffler/MD-FPCA"),
]

# ---- People ----
PEOPLE_INTRO = ('Our group develops statistical methodology for structured biomedical data, working closely with '
                'clinical collaborators across UCSF. Members are listed below.')
# --- PEOPLE: the People page ---------------------------------------------
# To add someone, copy the block from dict(name= down to its closing ),
# and paste it after. Photos go in the images folder.
PEOPLE = [
 dict(group="Principal Investigator", members=[
   dict(name=NAME, role=ROLE_FULL, img="headshot.jpg",
        bio="I develop Bayesian and functional-data methods for disease progression, multimodal neuroimaging, and "
            "high-dimensional structured regression, and serve as a core statistician for several centers at the "
            "UCSF Memory and Aging Center.",
        links=[("CV", CV),
               ("Google Scholar","https://scholar.google.com/citations?user=4aba0JUAAAAJ&hl=en"),
               ("Email","mailto:aaron.scheffler@ucsf.edu")]),
 ]),
 dict(group="Current Members", members=[
   dict(name="Raj", role="Professor, Department of Statistics, Texas A&amp;M University", img="raj-photo.jpg",
        bio="My research interests lie broadly in the development of Bayesian parametric and non-parametric "
            "methodology in complex biomedical and machine learning applications. My ongoing research focus is on "
            "scalable Bayesian methods for big data, dimensionality reduction, spatial/spatio-temporal statistics, "
            "and functional and object data (networks, tensor) analysis.",
        links=[]),
   dict(name="Isabella Pei", role="Senior, UC Berkeley &mdash; Computer Science, Cognitive Science &amp; Data Science",
        img="isabella-photo.jpeg",
        bio="I am a senior at UC Berkeley studying Computer Science, Cognitive Science, and Data Science. My "
            "current work focuses on developing Bayesian mixture models to characterize and predict Alzheimer&rsquo;s "
            "disease progression. My research interests lie broadly in the intersection of machine learning/"
            "computational modeling and healthcare.",
        links=[]),
   dict(name="Eric Yuzhe Jiang", role="Masters Student, Harvard University Institute for Applied Computational Science",
        img="eric-photo.jpg",
        bio="I am a graduate student at Harvard University&rsquo;s Institute for Applied Computational Science (IACS), "
            "focusing on the intersection of applied mathematics, data science, and computational biology. My current "
            "research with the group uses Bayesian mixture models to analyze Alzheimer&rsquo;s disease progression. "
            "Prior to Harvard, I earned my BA in Applied Mathematics from UC Berkeley. My research interests lie "
            "broadly in statistical methods, partial differential equations in fluids and biology, and numerical "
            "methods.",
        links=[]),
 ]),
 dict(group="Past Members", members=[
   dict(name="Yeseul", role="Assistant Professor, Department of Mathematics and Statistics", img="yeseul-photo.jpg",
        bio="My research focuses on developing explainable Bayesian deep learning methods that combine accurate "
            "prediction, statistical interpretability, and principled uncertainty quantification, particularly for "
            "high-dimensional spatial and biomedical data.",
        links=[]),
   dict(name="Rong Wu", role="PhD, Quantitative Biomedical Sciences", img="rong-photo.jpeg",
        bio="", links=[]),
 ]),
]
PEOPLE_JOIN = ('<strong>Interested in joining?</strong> I am glad to hear from prospective PhD students in the UCSF '
               'Epidemiology &amp; Biostatistics program, from postdoctoral candidates with a background in Bayesian '
               'methods or functional data analysis, and from clinical collaborators with structured data problems. '
               f'Email me at <a href="mailto:{EMAIL}">{EMAIL}</a> with a short note and your CV.')

# --- COURSES: the Teaching page ------------------------------------------
# Each entry is:
#     ("Code", "Course title", "Years", "Your role", "Description", None, "link"),
# Leave the None alone.
COURSES = [
 ("BIOSTAT 208","Biostatistical Methods for Clinical Research II","2023 &ndash; present","Course Director and Lecturer",
  "A second course in biostatistics focused on multi-predictor methods, including multiple linear and multiple logistic regression. Emphasis is on the practical and proper use of statistical methodology and its interpretation.",
  None,
  "https://epibiostat.ucsf.edu/biostatistical-methods-clinical-research-ii-biostat-208"),
 ("EBPS 121A&ndash;C","Epidemiology, Biostatistics and Population Sciences","2020 &ndash; present","Lecturer",
  "Core Inquiry Curriculum in the UCSF School of Medicine. EBPS covers the tools that all Domains of Understanding rely upon, allowing researchers and clinicians to interpret data and test hypotheses for complex questions.",
  None,
  "https://meded.ucsf.edu/bridges-curriculum"),
 ("PharmIS 110&ndash;112","Epidemiology, Biostatistics and Population Sciences","2023 &ndash; 2024","Lecturer",
  "Three lectures per year for first-year pharmacy students in the UCSF School of Pharmacy, covering introductory biostatistics, regression analysis, and meta-analysis.",
  None, "https://pharmacy.ucsf.edu/"),
 ("BIOSTAT 202","Opportunities and Challenges of Complex Biomedical Data","2019 &ndash; 2023","Course Director and Lecturer",
  "An introduction to the opportunities and challenges of using biological and health-related big data for biomedical research, including supervised and unsupervised machine learning.",
  None,
  "https://epibiostat.ucsf.edu/opportunities-and-challenges-complex-biomedical-data-introduction-science-big-data-biostat-202"),
]
TEACH_INTRO = 'I teach through the UCSF <a href="https://ticr.ucsf.edu/">Training in Clinical Research</a> program, the <a href="https://meded.ucsf.edu/bridges-curriculum">School of Medicine Bridges curriculum</a>, and the School of Pharmacy.'
TEACH_OUTRO = ('In 2024 I received the <strong>Excellence in Teaching</strong> award from the UCSF Training in Clinical '
               'Research Program, given to a single instructor each year, and the <strong>Dean’s Apple for Teachers</strong> '
               'award from the School of Pharmacy. I also serve as a faculty mentor in the UCSF K Scholars Program and on '
               'masters and doctoral committees in the Department of Epidemiology & Biostatistics.')
