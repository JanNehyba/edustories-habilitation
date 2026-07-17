# Kompletní seznam pro notebooky 10/20/30 a figury (auditováno proti library()
# a :: napříč analyzy/). grDevices je součást base R.
install.packages(c(
  "dplyr", "tidyr", "readr", "stringr",   # příprava a čtení dat (notebooky 10, 20)
  "readxl",                               # čtení xlsx (jen s raw daty; neškodí)
  "ggplot2",                              # figury (fig_*.R)
  "lme4", "lmerTest", "ordinal", "irr",   # smíšené modely a shoda (notebooky 30, 20)
  "knitr", "rmarkdown"                    # render Quarto notebooků
))
