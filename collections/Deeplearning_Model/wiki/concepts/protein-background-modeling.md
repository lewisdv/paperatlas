# Protein Background Modeling

## Definition

- Protein background modeling separates antibody-derived counts into target-specific biological signal and technical signal from ambient or nonspecific binding.
- It is especially important for CITE-seq because low protein counts need not imply absence of the corresponding cell-surface marker.

## In totalVI

- Each protein count is generated from a negative-binomial mixture with background and foreground components.
- The background mean and mixture probability vary by cell and protein.
- Cell state, RNA, the full protein panel, and batch therefore influence whether a particular count is treated as foreground.
- Denoising removes the expected background contribution while retaining a distribution over the remaining expression.

## Why A Global Cutoff Can Fail

- One protein-wide threshold assumes comparable background across cell types and droplets.
- Overlapping foreground and background distributions can produce false negatives, as reported for CD20, or false positives, as reported for CD28.
- Empty droplets, isotype controls, encoded RNA, and known cell-type markers provide partial validation signals, but none is complete ground truth.

## Downstream Consequences

- Background correction changes protein visualization, correlation, clustering, and differential-expression results.
- Statistical testing should integrate over model uncertainty rather than treating a single corrected matrix as observed data.
- A well-fitted mixture remains an assumption about the assay-generating process and can fail under new chemistries or antibody panels.

## Sources

- [Joint probabilistic modeling of single-cell multi-omic data with totalVI](../sources/gayoso_2021_totalvi_joint_probabilistic_multi-omic.md)
- [totalVI](../entities/totalVI.md)
