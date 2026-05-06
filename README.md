# Variant Analysis Pipeline

A comprehensive bioinformatics pipeline for detecting, filtering, and analyzing genetic variants from whole genome sequencing data.

## Overview

This project implements a complete variant analysis workflow including:
- **Read alignment** to reference genome using BWA
- **Variant calling** using bcftools
- **Quality filtering** based on sequencing metrics
- **Statistical analysis** and visualization of variant characteristics

## Project Structure

```
.
├── pipeline.sh              # Bash script for alignment and variant calling
├── varient.py              # Data preprocessing and parsing
├── scores.py               # Quality filtering and statistical analysis
├── rstplt.py               # Visualization and exploratory data analysis
├── variants_table.csv      # Raw variant data (VCF-like format)
├── high_quality_variants.csv  # Filtered high-quality variants
└── plots/                  # Output directory for visualizations
    ├── qual_distribution.png
    ├── depth_distribution.png
    ├── type_distribution.png
    └── dp_vs_qual.png
```

## Pipeline Components

### 1. Alignment & Variant Calling (`pipeline.sh`)

Aligns paired-end reads to a reference genome and calls variants:

**Steps:**
- BWA mem alignment of paired-end reads
- SAM to BAM conversion and sorting
- BAM indexing
- Variant calling with bcftools mpileup

**Requirements:**
- BWA
- SAMtools
- BCFtools
- Reference genome FASTA file

### 2. Data Preprocessing (`varient.py`)

Reads and parses raw variant data:
- Loads tab-separated variant calls
- Parses VCF-like format into structured DataFrame
- Extracts core variant information

**Output:** Parsed variant data with columns:
- CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO, FORMAT, SAMPLE

### 3. Quality Filtering & Analysis (`scores.py`)

Applies quality control filters and statistical analysis:

**Filtering Criteria:**
- Quality score (QUAL) > 50
- Read depth (DP) > 10

**Analysis Performed:**
- Quality distribution before/after filtering
- Read depth distribution before/after filtering
- SNP vs INDEL classification
- Variant removal statistics

**Output:** `high_quality_variants.csv` - Filtered variants meeting QC thresholds

### 4. Visualization (`rstplt.py`)

Generates exploratory plots for quality assessment:

**Plots Created:**
- **qual_distribution.png** - Histogram of quality scores for high-quality variants
- **depth_distribution.png** - Histogram of read depth
- **type_distribution.png** - Bar chart comparing SNP vs INDEL counts
- **dp_vs_qual.png** - Scatter plot showing relationship between depth and quality

## Installation

### Python Dependencies

```bash
pip install pandas numpy matplotlib
```

### System Tools (for pipeline.sh)

```bash
# Ubuntu/Debian
sudo apt-get install bwa samtools bcftools

# macOS (using brew)
brew install bwa samtools bcftools
```

## Usage

### Complete Workflow

Run the full pipeline:

```bash
# 1. Variant calling (alignment + calling)
bash pipeline.sh

# 2. Data preprocessing
python varient.py

# 3. Quality filtering and analysis
python scores.py

# 4. Visualization
python rstplt.py
```

### Individual Scripts

Run individual analysis steps as needed:

```bash
# Just create visualizations from existing high-quality variants
python rstplt.py

# Re-run quality filtering from raw variants
python scores.py
```

## Data Format

### Input Format (variants_table.csv)

Tab-separated VCF-like format:
```
CHROM  POS    ID    REF    ALT    QUAL   FILTER   INFO           FORMAT   SAMPLE
22     12345  .     A      G      60     PASS     DP=50;AF=0.5    GT:DP    0/1:50
```

### Output Format (high_quality_variants.csv)

Filtered variants with added TYPE column:
```
CHROM,POS,ID,REF,ALT,QUAL,FILTER,INFO,FORMAT,SAMPLE,TYPE
22,12345,.,A,G,60,PASS,DP=50;AF=0.5,GT:DP,0/1:50,SNP
```

## Quality Metrics

### Variant Type Classification
- **SNP (Single Nucleotide Polymorphism):** REF length = 1 AND ALT length = 1
- **INDEL (Insertion/Deletion):** All other cases

### QC Thresholds
- **QUAL > 50:** Ensures high-confidence variant calls
- **DP > 10:** Requires minimum 10x read depth for robust genotyping

## Output Summary

The analysis produces:

| Metric | Source |
|--------|--------|
| Original variant count | scores.py output |
| High-quality count | high_quality_variants.csv |
| Variants removed | scores.py output |
| Quality improvement | Before/after QUAL mean comparison |
| SNP vs INDEL ratio | type_distribution.png |

## Example Results

```
Original variants: 1,245
Filtered variants: 892
Variants removed: 353 (28%)
Mean QUAL before: 45.2
Mean QUAL after: 62.1
Mean DP before: 8.5
Mean DP after: 22.3
```

## Future Improvements

- **Variant Annotation** - Integrate tools like VEP (Variant Effect Predictor) or ANNOVAR for functional annotation of variants, identifying their biological impact and association with known disease databases
- **Machine Learning-based Classification** - Implement ML models to classify variants by pathogenicity, using features like quality scores, allele frequency, and predicted functional effects for automated variant prioritization

## Notes

- Variant positions are 1-based
- All scripts assume input files are in the same directory
- Plots are saved to the `plots/` directory
- See individual script comments for detailed parameter explanations

## Author

Aryan Khadse
Bioinformatics Enthusiast | Computational Biology | Genomic Data Analysis
GitHub: ABIO-BY-ARYAN05
