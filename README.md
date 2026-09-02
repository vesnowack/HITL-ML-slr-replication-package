# Replication package: Understanding the ``Human'' in the Loop - A Systematic Literature Review in Software Engineering

This package contains the data, search results, screening decisions, quality assessments, and extracted data supporting the paper *[paper title]*. It allows a reader to inspect and reproduce the study selection process and the results reported for each research question.

## What this package includes

- Raw and filtered search results per venue
- Screening decisions (inclusion/exclusion) for every candidate paper
- Quality assessment scores for all included studies
- Extracted/coded data used to answer each RQ
- Source data and scripts for the tables and figures in the paper

## Repository structure

```
/search-results/
    ASE.csv                     raw search results for ASE
    FSE.csv                     raw search results for FSE
    ...
    keyword-search-log.md       manual search keyword iteration log

/screening/
    included-papers.csv         full-text review outcome for papers that passed screening and were included in the review

/data-extraction/
    codebook.md                 definitions of all extracted fields
    rq1-roles.csv
    rq2-interactions.csv
    rq3-quality-attributes.csv
    rq4-evaluation-metrics.csv

/figures/
    venue-table-source.csv      source data for Table: venue counts
    fig-history-source.csv      source data for the by-year/by-type figures
    generate-figures.py         script to regenerate the figures from source data

/primary-studies.csv            full list of the 51 included studies
                                 (citation, DOI/link, venue, year, source: AS/SB)

README.md                       this file
```

## Research questions

- **RQ1.** What design roles do human agents play in HITL machine learning systems?
- **RQ2.** What types of human-agent interactions are supported by existing HITL software architectures?
- **RQ3.** What software quality attributes are prioritized when designing HITL systems, and do they reflect human-centric concerns?
- **RQ4.** What evaluation metrics are used to assess the effectiveness and quality of HITL system designs?
- **RQ5.** To what extent has the rise of LLMs and generative AI impacted the design of HITL systems?

## Search and selection methodology

**Search period.** January 2015 – December 2025.

**Search strategy.** A combination of manual and automated search, following the Quasi-Gold Standard (QGS) approach (Zhang et al.). The manual search identified keyword terms and relevant venues; the automated search complemented it using a keyword-based query against IEEE Xplore, ACM Digital Library, and Science Direct.

**Automated search query:**
```
("human-in-the-loop" OR "human in the loop" OR "Active learning" OR
 "mixed-initiative learning" OR "interactive learning") AND
("machine learning" OR "learning")
```

**Manual search keywords:** human, loop, active, interactive, mixed-initiative, query, robust-, verifi-, guarante-, explain-, interpret-, shift, streams, decision-support, oracle, suggest-, recommend-, learn-, synthesis, hybrid, crowd-, collabor-, teach-, feedback, iterat-, guid-

**Venues searched.** 11 top-tier Software Engineering venues (5 conferences, 3 symposia, 3 journals), ranked A*/A in CORE or Q1 in Scimago. Full list and per-venue counts are in `search-results/` and `figures/venue-table-source.csv`.

**Note on scope.** Springer, arXiv, and DBLP were not searched directly — Springer indexes a large volume of AI venues outside our SE scope, and arXiv/DBLP are not peer-reviewed sources and fell outside our quality criteria. Relevant work from these sources was captured indirectly, where it met the inclusion criteria, through the manual search and snowballing.

### Inclusion criteria

| ID | Criterion |
|---|---|
| I1 | Published between January 2015 and December 2025 |
| I2 | Published in one of the top-tier Software Engineering venues |
| I3 | Classified as a full paper (technical or experience) if published in conference proceedings |
| I4 | Describes a system that includes a human and an ML agent |
| I5 | Describes a system involving iterative interaction between the human and ML agents |

### Exclusion criteria

| ID | Criterion |
|---|---|
| E1 | Editorial, extended abstract, position paper, short paper, tool paper, poster summary, keynote, survey, opinion, tutorial/conference/workshop/panel summary |
| E2 | Published in a venue without a full peer-review process |
| E3 | Describes an ML model trained/modified offline without human involvement |
| E4 | No explicit investigation into human involvement |
| E5 | Keywords appear in the title with a different meaning than intended here |

## Study selection results

| Stage | Count |
|---|---|
| Articles initially screened across all venues | 14,832 |
| Full-text reviewed | 1,306 |
| Included via automated search (AS) | 47 |
| Included via snowball search (SB) | 4 |
| **Total primary studies** | **51** |

The full list of 51 primary studies, with citation details and DOI/link, is in `primary-studies.csv`.

## Quality assessment

Each included study was scored against six quality criteria, each on a three-point scale (No = 1, Partially = 2, Yes = 3):

| ID | Criterion |
|---|---|
| QC1 | Is the study highly relevant to the objectives of the SLR? |
| QC2 | Does the study clearly state its research aims? |
| QC3 | Does the study provide an adequate review of relevant prior work? |
| QC4 | Is the research methodology clearly described? |
| QC5 | Is the experimental design appropriate? |
| QC6 | Does the research add value to the academic or industrial community? |

All included studies met the quality bar; no studies were excluded at this stage.

## Data extraction and coding

`data-extraction/codebook.md` defines every field extracted per paper. Extraction was organised per RQ:

- `rq1-roles.csv` — human role classification per study
- `rq2-interactions.csv` — human-agent interaction types per study
- `rq3-quality-attributes.csv` — software quality attributes discussed per study
- `rq4-evaluation-metrics.csv` — evaluation metrics used per study

## Reproducing figures and tables

```bash
cd figures
python generate-figures.py
```

This regenerates the venue table and the by-year/by-type distribution figures from the source CSVs. Requires Python 3.x with `pandas` and `matplotlib` ([TODO: add exact versions once pinned]).

