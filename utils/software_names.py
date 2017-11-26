'''
Created on Nov 26, 2017

@author: mmp
'''

import os

class SoftwareNames(object):
	'''
	classdocs
	'''

	## dir with software
	DIR_SOFTWARE = "/usr/local/software/insaflu"
	SOFTWARE_SAMTOOLS = os.path.join(DIR_SOFTWARE, "snippy/bin/samtools")
	SOFTWARE_SAMTOOLS_name = "Samtools"
	SOFTWARE_SAMTOOLS_VERSION = "1.3"
	SOFTWARE_SAMTOOLS_PARAMETERS = ""
	SOFTWARE_BGZIP = os.path.join(DIR_SOFTWARE, "snippy/bin/bgzip")
	SOFTWARE_BGZIP_name = "bgzip"
	SOFTWARE_BGZIP_VERSION = "1.3"
	SOFTWARE_BGZIP_PARAMETERS = ""
	SOFTWARE_TABIX = os.path.join(DIR_SOFTWARE, "snippy/bin/tabix")
	SOFTWARE_TABIX_name = "tabix"
	SOFTWARE_TABIX_VERSION = "1.3"
	SOFTWARE_TABIX_PARAMETERS = ""
	SOFTWARE_SPAdes = os.path.join(DIR_SOFTWARE, "SPAdes-3.11.1-Linux/bin/spades.py") 
	SOFTWARE_SPAdes_name = "SPAdes" 
	SOFTWARE_SPAdes_VERSION = "3.11.1"
	SOFTWARE_SPAdes_PARAMETERS = ""
	SOFTWARE_ABRICATE = os.path.join(DIR_SOFTWARE, "abricate/bin/abricate")
	SOFTWARE_ABRICATE_name = "Abricate"
	SOFTWARE_ABRICATE_DB = os.path.join(DIR_SOFTWARE, "abricate/db")
	SOFTWARE_ABRICATE_VERSION = "0.8-dev"
	SOFTWARE_ABRICATE_PARAMETERS = ""
	SOFTWARE_FASTQ = os.path.join(DIR_SOFTWARE, "FastQC/fastqc")
	SOFTWARE_FASTQ_name = "FastQC"
	SOFTWARE_FASTQ_VERSION = "0.11.5"
	SOFTWARE_FASTQ_PARAMETERS = ""
	SOFTWARE_TRIMMOMATIC = os.path.join(DIR_SOFTWARE, "trimmomatic/classes/trimmomatic.jar")
	SOFTWARE_TRIMMOMATIC_name = "Trimmomatic"
	SOFTWARE_TRIMMOMATIC_VERSION = "0.27"
	SOFTWARE_TRIMMOMATIC_PARAMETERS = "SLIDINGWINDOW:5:20 LEADING:3 TRAILING:3 MINLEN:55 TOPHRED33"
	SOFTWARE_SNIPPY = os.path.join(DIR_SOFTWARE, "snippy/bin/snippy")
	SOFTWARE_SNIPPY_name = "Snippy"
	SOFTWARE_SNIPPY_VERSION = "3.2-dev"
	SOFTWARE_SNIPPY_PARAMETERS = "--mapqual 20 --mincov 10 --minfrac 0.51"
	SOFTWARE_SNIPPY_VCF_TO_TAB = os.path.join(DIR_SOFTWARE, "snippy/bin/snippy-vcf_to_tab_add_freq")
	SOFTWARE_SNIPPY_VCF_TO_TAB_name = "Snippy-vcf_to_tab_add_freq"
	SOFTWARE_SNIPPY_VCF_TO_TAB_VERSION = "3.2-dev"
	SOFTWARE_SNIPPY_VCF_TO_TAB_PARAMETERS = ""
	SOFTWARE_SNP_EFF = os.path.join(DIR_SOFTWARE, "snippy/bin/snpEff")
	SOFTWARE_SNP_EFF_config = os.path.join(DIR_SOFTWARE, "snippy/etc/snpeff.config")
	SOFTWARE_SNP_EFF_name = "snpEff"
	SOFTWARE_SNP_EFF_VERSION = "4.3p"
	SOFTWARE_SNP_EFF_PARAMETERS = "-no-downstream -no-upstream -no-intergenic -no-utr -noStats"
	SOFTWARE_GENBANK2GFF3 = 'bp_genbank2gff3'
	SOFTWARE_GENBANK2GFF3_name = 'Genbank2gff3'
	SOFTWARE_GENBANK2GFF3_VERSION = 'Unknown'
	SOFTWARE_GENBANK2GFF3_PARAMETERS = ''
	SOFTWARE_FREEBAYES = os.path.join(DIR_SOFTWARE, "snippy/bin/freebayes")
	SOFTWARE_FREEBAYES_name = "Freebayes"
	SOFTWARE_FREEBAYES_VERSION = "v1.1.0-54-g49413aa"
	SOFTWARE_FREEBAYES_PARAMETERS = "-p 2 -q 20 -m 20 --min-coverage 100 --min-alternate-fraction 0.01 --min-alternate-count 10 -V"
	SOFTWARE_COVERAGE = "Coverage, in-house script"
	SOFTWARE_COVERAGE_name = "Coverage"
	SOFTWARE_COVERAGE_VERSION = "v1.1"
	SOFTWARE_COVERAGE_PARAMETERS = ""
	
	SOFTWARE_PROKKA = os.path.join(DIR_SOFTWARE, "prokka/bin/prokka")
	SOFTWARE_PROKKA_name = "Prokka"
	SOFTWARE_PROKKA_VERSION = "1.2"
	SOFTWARE_PROKKA_PARAMETERS = "--kingdom Viruses --locustag locus --genus Influenzavirus --species Influenzavirus --strain ref_PREFIX_FILES_OUT"
	
	SOFTWARE_MAUVE = os.path.join(DIR_SOFTWARE, "mauve/progressiveMauve")
	SOFTWARE_MAUVE_name = "Mauve"
	SOFTWARE_MAUVE_VERSION = "Feb 13 2015 at 05:57:13"
	SOFTWARE_MAUVE_PARAMETERS = ""
	
	SOFTWARE_CONVERT = os.path.join(DIR_SOFTWARE, "scripts/convert.pl")
	SOFTWARE_CONVERT_name = "Convert"
	SOFTWARE_CONVERT_VERSION = ""
	SOFTWARE_CONVERT_PARAMETERS = ""

	SOFTWARE_MAFFT = os.path.join(DIR_SOFTWARE, "mafft-7.313-without-extensions/scripts/mafft")
	SOFTWARE_SET_ENV_MAFFT = "export MAFFT_BINARIES={}".format(os.path.join(DIR_SOFTWARE, "mafft-7.313-without-extensions/binaries"))
	SOFTWARE_MAFFT_name = "Mafft"
	SOFTWARE_MAFFT_VERSION = "7.313"
	SOFTWARE_MAFFT_PARAMETERS = ""
	
	SOFTWARE_FASTTREE = os.path.join(DIR_SOFTWARE, "fasttree/FastTree")
	SOFTWARE_FASTTREE_name = "FastTree"
	SOFTWARE_FASTTREE_VERSION = "2.1.10 SSE3"
	SOFTWARE_FASTTREE_PARAMETERS = "-gtr -boot 1000 -nt"
	
	def __init__(self):
		'''
		Constructor
		'''
		pass

	"""
	return samtools software
	"""
	def get_samtools(self): return self.SOFTWARE_SAMTOOLS
	def get_samtools_version(self): return self.SOFTWARE_SAMTOOLS_VERSION

	"""
	return spades software
	"""
	def get_spades(self): return self.SOFTWARE_SPAdes
	def get_spades_name(self): return self.SOFTWARE_SPAdes_name
	def get_spades_version(self): return self.SOFTWARE_SPAdes_VERSION
	def get_spades_parameters(self): return self.SOFTWARE_SPAdes_PARAMETERS

	"""
	return abricate software
	"""
	def get_abricate(self): return self.SOFTWARE_ABRICATE
	def get_abricate_name(self): return self.SOFTWARE_ABRICATE_name
	def get_abricate_version(self): return self.SOFTWARE_ABRICATE_VERSION
	def get_abricate_parameters(self): return self.SOFTWARE_ABRICATE_PARAMETERS

	"""
	return FASTq software
	"""
	def get_fastq(self): return self.SOFTWARE_FASTQ
	def get_fastq_name(self): return self.SOFTWARE_FASTQ_name
	def get_fastq_version(self): return self.SOFTWARE_FASTQ_VERSION
	def get_fastq_parameters(self): return self.SOFTWARE_FASTQ_PARAMETERS
	
	"""
	return trimmomatic software
	"""
	def get_trimmomatic(self): return self.SOFTWARE_TRIMMOMATIC
	def get_trimmomatic_name(self): return self.SOFTWARE_TRIMMOMATIC_name
	def get_trimmomatic_version(self): return self.SOFTWARE_TRIMMOMATIC_VERSION
	def get_trimmomatic_parameters(self): return self.SOFTWARE_TRIMMOMATIC_PARAMETERS
	
	"""
	return snippy software
	"""
	def get_snippy(self): return self.SOFTWARE_SNIPPY
	def get_snippy_name(self): return self.SOFTWARE_SNIPPY_name
	def get_snippy_version(self): return self.SOFTWARE_SNIPPY_VERSION
	def get_snippy_parameters(self): return self.SOFTWARE_SNIPPY_PARAMETERS

	"""
	return snippy-vcf_to_tab software
	"""
	def get_snippy_vcf_to_tab(self): return self.SOFTWARE_SNIPPY_VCF_TO_TAB
	def get_snippy_vcf_to_tab_name(self): return self.SOFTWARE_SNIPPY_VCF_TO_TAB_name
	def get_snippy_vcf_to_tab_version(self): return self.SOFTWARE_SNIPPY_VCF_TO_TAB_VERSION
	def get_snippy_vcf_to_tab_parameters(self): return self.SOFTWARE_SNIPPY_VCF_TO_TAB_PARAMETERS
	
	"""
	return snpEff software
	"""
	def get_snp_eff(self): return self.SOFTWARE_SNP_EFF
	def get_snp_eff_name(self): return self.SOFTWARE_SNP_EFF_name
	def get_snp_eff_config(self): return self.SOFTWARE_SNP_EFF_config
	def get_snp_eff_version(self): return self.SOFTWARE_SNP_EFF_VERSION
	def get_snp_eff_parameters(self): return self.SOFTWARE_SNP_EFF_PARAMETERS
	
	"""
	return genbank2gff3 software
	"""
	def get_genbank2gff3(self): return self.SOFTWARE_GENBANK2GFF3
	def get_genbank2gff3_name(self): return self.SOFTWARE_GENBANK2GFF3_name
	def get_genbank2gff3_version(self): return self.SOFTWARE_GENBANK2GFF3_VERSION
	def get_genbank2gff3_parameters(self): return self.SOFTWARE_GENBANK2GFF3_PARAMETERS
	
	
	"""
	return freebayes software
	"""
	def get_freebayes(self): return self.SOFTWARE_FREEBAYES
	def get_freebayes_name(self): return self.SOFTWARE_FREEBAYES_name
	def get_freebayes_version(self): return self.SOFTWARE_FREEBAYES_VERSION
	def get_freebayes_parameters(self): return self.SOFTWARE_FREEBAYES_PARAMETERS

	"""
	return bgzip software
	"""
	def get_bgzip(self): return self.SOFTWARE_BGZIP
	def get_bgzip_name(self): return self.SOFTWARE_BGZIP_name
	def get_bgzip_version(self): return self.SOFTWARE_BGZIP_VERSION
	def get_bgzip_parameters(self): return self.SOFTWARE_BGZIP_PARAMETERS

	"""
	return tabix software
	"""
	def get_tabix(self): return self.SOFTWARE_TABIX
	def get_tabix_name(self): return self.SOFTWARE_TABIX_name
	def get_tabix_version(self): return self.SOFTWARE_TABIX_VERSION
	def get_tabix_parameters(self): return self.SOFTWARE_TABIX_PARAMETERS
	
	"""
	return Coverage software
	"""
	def get_coverage(self): return self.SOFTWARE_COVERAGE
	def get_coverage_name(self): return self.SOFTWARE_COVERAGE_name
	def get_coverage_version(self): return self.SOFTWARE_COVERAGEVERSION
	def get_coverage_parameters(self): return self.SOFTWARE_COVERAGE_PARAMETERS
	
	"""
	return Prokka software
	"""
	def get_prokka(self): return self.SOFTWARE_PROKKA
	def get_prokka_name(self): return self.SOFTWARE_PROKKA_name
	def get_prokka_version(self): return self.SOFTWARE_PROKKA_VERSION
	def get_prokka_parameters(self): return self.SOFTWARE_PROKKA_PARAMETERS

	"""
	return Mauve software
	"""
	def get_mauve(self): return self.SOFTWARE_MAUVE
	def get_mauve_name(self): return self.SOFTWARE_MAUVE_name
	def get_mauve_version(self): return self.SOFTWARE_MAUVE_VERSION
	def get_mauve_parameters(self): return self.SOFTWARE_MAUVE_PARAMETERS

	"""
	return Convert Mauve software
	"""
	def get_convert_mauve(self): return self.SOFTWARE_CONVERT
	def get_convert_mauve_name(self): return self.SOFTWARE_CONVERT_name
	def get_convert_mauve_version(self): return self.SOFTWARE_CONVERT_VERSION
	def get_convert_mauve_parameters(self): return self.SOFTWARE_CONVERT_PARAMETERS
	
	"""
	return Mafft software
	"""
	def get_mafft(self): return self.SOFTWARE_MAFFT
	def get_mafft_set_env_variable(self): return self.SOFTWARE_SET_ENV_MAFFT
	def get_mafft_name(self): return self.SOFTWARE_MAFFT_name
	def get_mafft_version(self): return self.SOFTWARE_MAFFT_VERSION
	def get_mafft_parameters(self): return self.SOFTWARE_MAFFT_PARAMETERS
	
	"""
	return FastTree software
	"""
	def get_fasttree(self): return self.SOFTWARE_FASTTREE
	def get_fasttree_name(self): return self.SOFTWARE_FASTTREE_name
	def get_fasttree_version(self): return self.SOFTWARE_FASTTREE_VERSION
	def get_fasttree_parameters(self): return self.SOFTWARE_FASTTREE_PARAMETERS


