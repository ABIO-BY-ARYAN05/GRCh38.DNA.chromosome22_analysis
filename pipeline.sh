#!/bin/bash
echo "samtool execution protocol"
set -e

REF="Homo_sapiens.GRCh38.dna.chromosome.22.fa"
R1="SRR362015_1.fastq.gz"
R2="SRR362015_2.fastq.gz"
echo "Starting pipeline..."

bwa mem $REF $R1 $R2 > aln.sam

samtool faidx $REF
samtools view -S -b aln.sam > output.bam
samtools sort output.bam -o sorted.bam
samtools index sorted.bam

bcftools mpileup -f reference.fa sorted.bam | bcftools call -mv -o variants.vcf

echo "samtool execution completed!"
