# Replication package: Understanding the "Human" in the Loop - A Systematic Literature Review in Software Engineering

This package contains the data, search results, screening decisions, and
extracted data supporting the paper *the "Human" in the Loop - 
A Systematic Literature Review in Software Engineering*. It allows a reader to
inspect and reproduce the study selection process and the results reported
for each research question.

## What this package includes

- Raw search results per venue
- The full list of the 50 primary studies included in the review
- Extracted/coded data used to answer each RQ
- Source data and scripts for the tables and figures in the paper

## Repository structure

```
/search-results/
    venue-search-summary.xlsx  per-venue digital library, search string, search
                               period, access date, papers returned by the
                               search, and papers included in the final review
    ASE.xlsx, FSE.xlsx, ICSE.xlsx, ICST.xlsx, SANER.xlsx, ISSRE.xlsx,
    ISSTA.xlsx, SEAMS.xlsx, IST.xlsx, TOSEM.xlsx, TSE.xlsx
                               per-venue full-text screening record: one row
                               per reviewed candidate (title, authors, link,
                               inclusion decision, and RQ1-RQ4 coding, reviewer name, exclusion-reason,
                               and free-text comment columns from the working
                               sheets are not included here); row counts match
                               the "Reviewed" column in the venue table in
                               04_methodology.tex exactly

/data-extraction/
    rq1-roles.csv
    rq2-interactions.csv
    rq3-quality-attributes.csv
    rq4-evaluation-metrics.csv

/figures/
    venue-table-source.csv          source data for the venue table (Table "papers" in 04_methodology.tex)
    article_numbers.png, article_distribution.png, sankey_rq_combinations.png   the exact figure files as currently shipped in the paper
    sankey_rq_combinations_reproduction.html   freshly generated from the extraction CSVs (see note below)

/scripts/
    generate-figures.py             regenerates ../figures/article_numbers.png, ../figures/article_distribution.png
    generate-sankey.py              regenerates ../figures/sankey_rq_combinations_reproduction.png

/primary-studies.csv            full list of the 50 included studies
                                 (citation key, title, authors, year, venue, link, source: automated search(AS)/snowballing(SB))

README.md                       this file
```

## Research questions

- **RQ1.** What design roles are assigned to human agents in HITL machine-learning systems?
- **RQ2.** What types of actions do human agents perform in their interactions with ML agents?
- **RQ3.** What software quality attributes are considered when designing HITL machine-learning systems, and how do these account for human participation?
- **RQ4.** What evaluation metrics are used to assess HITL machine-learning systems, and what aspects of the human-ML system do they capture?

The paper additionally discusses, outside the systematic review itself, how
LLM- and agentic-AI systems are changing the broader conception of
human-in-the-loop (Section "The changing locus of human involvement in the
LLM and agentic era"). That discussion uses the RQ1-RQ4 dimensions as
analytical lenses over contextual literature and is explicitly not a
systematic sample -- see `09_threats.tex` in the main repository ("Contextual
literature outside the systematic corpus").

## Search and selection methodology

**Search period.** January 2015 - December 2025.

**Search strategy.** A combination of manual and automated search: the manual search
identified keyword terms and relevant venues; the automated search complemented
it using a keyword-based query against IEEE Xplore, ACM Digital Library, and
Science Direct.

**Automated search query:**
```
("human-in-the-loop" OR "human in the loop" OR "Active learning" OR
 "mixed-initiative learning" OR "interactive learning") AND
("machine learning" OR "learning")
```

**Manual search keywords:** human, loop, active, interactive, mixed-initiative,
query, robust-, verifi-, guarante-, explain-, interpret-, shift, streams,
decision-support, oracle, suggest-, recommend-, learn-, synthesis, hybrid,
crowd-, collabor-, teach-, feedback, iterat-, guid-

**Venues searched.** 11 top-tier Software Engineering venues (5 conferences, 3
symposia, 3 journals), ranked A*/A in CORE or Q1 in Scimago. Full list and
per-venue counts are in `search-results/` and `figures/venue-table-source.csv`.

### Inclusion criteria

| ID | Criterion |
|---|---|
| I1 | The article is published in the period between January 2015 - December 2025. |
| I2 | The article is published in one of the top-tier venues in Software Engineering. |
| I3 | The article is classified as a full paper (technical or experience) if published in conference proceedings. |
| I4 | The article describes a system that includes a human and an ML agent. |
| I5 | The article describes a system in which human involvement forms part of an iterative interaction process with the ML agent. |
| I6 | The article describes a system in which information arising from the human's behaviour, judgement, feedback, correction, or other contribution is used to train or refine the ML agent. |

### Exclusion criteria

| ID | Criterion |
|---|---|
| E1 | Articles classified as editorial, extended abstracts, position papers, short papers, tool papers, poster summaries, keynotes, surveys, opinions, tutorial summaries, conference summaries (or introductions to conference proceedings or journal issues), workshop summaries or panel summaries. |
| E2 | Articles from venues that do not apply a full peer-review process. |
| E3 | Articles describing systems where the ML model is trained or modified offline without human involvement, such as through hyper-parameter tuning or architectural changes. |
| E4 | Articles describing systems without an explicit investigation into human involvement. |
| E5 | Articles in which the keywords identified above appear in the title but have different meanings from those intended in this review. |


## Study selection results

| Stage | Count |
|---|---:|
| Articles initially screened across all venues | 14,832 |
| Full-text reviewed | 1,306 |
| Included via automated search (AS) | 46 |
| Included via snowball search (SB) | 4 |
| &nbsp;&nbsp;-- backward snowball | 2 |
| &nbsp;&nbsp;-- forward snowball | 2 |
| **Total primary studies** | **50** |

The full list of 50 primary studies, with citation details and link, is in
`primary-studies.csv`.

## Quality assessment

Each paper that passed screening was assessed against six quality criteria,
each scored on a three-point scale (No = 1, Partially = 2, Yes = 3):

| ID | Criterion |
|---|---|
| QC1 | Is the study highly relevant to the objectives of the SLR? |
| QC2 | Does the study clearly state its research aims? |
| QC3 | Does the study provide an adequate review of relevant prior work? |
| QC4 | Is the research methodology clearly described? |
| QC5 | Is the experimental design appropriate? |
| QC6 | Does the research add value to the academic or industrial community? |

All criteria were equally weighted; the six scores per paper were aggregated
and normalised to an overall quality score from 1 to 5. All assessed papers
achieved a high overall score, so none were excluded at this stage. Per-study
scores were not found in the working repository, so they are not included as
a data file here.

## Data extraction and coding

Extraction was organised per RQ:

- `rq1-roles.csv` -- human role classification per study
- `rq2-interactions.csv` -- human-agent interaction types per study
- `rq3-quality-attributes.csv` -- software quality attributes discussed per study
- `rq4-evaluation-metrics.csv` -- evaluation metrics used per study

## Reproducing figures and tables

```bash
cd scripts
python3 generate-figures.py             # ../figures/article_numbers.png, ../figures/article_distribution.png
python3 generate-sankey.py              # ../figures/sankey_rq_combinations_reproduction.png/.html (reproduction -- see note above)
```

Requires Python 3.x with `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`
(and, for static Sankey PNG export, a working `kaleido` install --
`pip install 'plotly[kaleido]'`; the HTML output does not need it).
