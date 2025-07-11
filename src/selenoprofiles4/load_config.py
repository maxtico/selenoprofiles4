
selenoprofiles_config_content="""##### selenoprofiles_4 configuration file. For a description of each options see selenoprofiles_4.py --help full 
### folders. r is the default result folder name 

selenoprofiles_data_dir = ~/selenoprofiles_data/
ncpus = 1
temp = /tmp/

profiles_folder = {selenoprofiles_data_dir}/selenoprotein_profiles
bin_folder =  
o = selenoprofiles_results

# save extracted scaffolds in temp folder (1) or trash everything at each run (0)?
save_chromosomes=0
## default profile. Searched in profiles_folder. Many possible type of value as argument (see -help)
profile=

### default: maximum sensitivity. Turn genewise_to_be_sure = 0 for more speed, dont_genewise = 1 for max speed.
#dont_exonerate = 0         
dont_genewise  = 0        
genewise_to_be_sure = 1

### active output format
output_ali=1
output_p2g=1
#output_fasta=0
#output_cds=0
#output_gff=0
## etc... view -help

## this much sequence in gene surroundings is extracted for each result and can be used by actions or output 
three_prime_length=6000
five_prime_length=10

### actions: improving predictions
ACTION.pre_choose._improve1       =     if not opt['no_splice'] and x.prediction_program()=='blast':    x.remove_internal_introns(min_length=18)
ACTION.pre_choose._improve2       =     if not opt['no_splice']: x.clean_inframe_stop_codons(max_codons_removed=10)
ACTION.pre_choose._improve3       =     x.exclude_large_introns(max_intron_length=140000)
ACTION.post_filtering._improve4   =     if x.filtered == 'kept': x.complete_at_three_prime(max_extension=300, max_query_unaligned=3000)
ACTION.post_filtering._improve5   =     if x.filtered == 'kept': x.complete_at_five_prime( max_extension=300, max_query_unaligned=3000, full=True)
#ACTION.post_filtering.secisearch  =     if x.filtered == 'kept' and x.profile.has_selenocysteine() and x.label in ['selenocysteine', 'unaligned', 'uga_containing', 'pseudo']:  Secisearch3(x) 
#ACTION.post_filtering.bsecisearch  =     if x.filtered == 'kept' and x.profile.has_selenocysteine() and x.label in ['selenocysteine', 'uga_containing', 'pseudo']:  bSecisearch(x)

## database settings. if you want to inspect any result filtered out you must have full_db = 1
max_attempts_database  = 500
sleep_time             = 10
full_db                = 0

### setting defaults and keywords for profile attributes.    
##  default filtering procedures for blast hits and for final p2g candidates  
blast_filtering.DEFAULT     =     x.evalue < 1e-2  or x.sec_is_aligned()
p2g_filtering.DEFAULT       =     len(x.protein()) >60 or x.coverage()> 0.4
p2g_refiltering.DEFAULT     =     x.awsi_filter()

## max number of blast hits kept. a warning if printed if passed. set blast_filtering_warning = 0 to crash instead
max_blast_hits.DEFAULT                    = 2500
max_blast_hits.STRICT                     = 100 
max_blast_hits.LARGE                      = 10000 
blast_filtering_warning = 1

##  genetic code
genetic_code = 1 

###  program options (same for all profiles). -a is for number of cpus
blast_opt     = -a {ncpus}
exonerate_opt =
genewise_opt  =

# never change blast option  -F F : psitblastn will crash
blast_options.DEFAULT       =   -b 5000 -F F 
exonerate_options.DEFAULT   =   
genewise_options.DEFAULT    =   -codon {selenoprofiles_install_dir}/wisecfg/codon.table.gc{genetic_code}.std
# keyword SELENO: specifying custom options for certain profiles
blast_options.SELENO        =   -b 5000 -F F 
exonerate_options.SELENO    =   -M {selenoprofiles_install_dir}/exoneratecfg/BLOSUM62sel 
genewise_options.SELENO     =   -m {selenoprofiles_install_dir}/wisecfg/BLOSUM62sel.bla -codon {selenoprofiles_install_dir}/wisecfg/codon.table.gc{genetic_code}.sec

# technical, and advanced filtering
clustering_seqid.DEFAULT                  = 0.27
max_column_gaps.DEFAULT                   = 0.55
tags.DEFAULT                =    []
tag_db.DEFAULT              =    {selenoprofiles_data_dir}/uniref50_seleno_sim.fasta
uniref2go_db.DEFAULT        =    {selenoprofiles_data_dir}/gene_ontology/idmapping_uniref_GO.tab
tag_blast_options.DEFAULT   =    -F "m S" -a {ncpus} -f 999  -e 1e-10 -M BLOSUM80 -G 9 -E 2 
neutral_tags.DEFAULT        =     ['hypothet?ical',  'hypothet?ical conserved protein',  'PREDICTED',  'unnamed protein product',  'unknown',  'putative',  '(gi\\|.*\\| RIKEN cDNA .+ (gene)?(protein)? \\[.+\\].?)+$',  '(gi\\|.*\\| +([a-zA-Z0-9\\-]+) \\[Drosophila .+\\].*)+',  '(gi\\|.*\\| +(AGAP[a-zA-Z0-9\\-]+) \\[Anopheles .+\\].*)+',  'chromosome \\w+ open reading frame \\w+, isoform CRA',  '\\wCG\\d+(, isoform CRA_.+)? \\[.+\\]',  '(gi\\|.*\\| +SJ[a-zA-Z0-9\\-]+ +(protein)? +\\[Schistosoma japonicum].*)+',  'gi\\|.*\\| +MGC\\d+ (protein )?\\[Xenopus .+\\]',  'Uncharacterized protein']

#gene extensions for cyclic exonerate and genewise
exonerate_extension = 200000
genewise_extension  = 100
genewise_tbs_extension = 10000
GO_obo_file            = {selenoprofiles_data_dir}/gene_ontology/gene_ontology_ext.obo

## defining built-in sets of families. follow the syntax to create custom sets
families_set.prokarya = ahpd,ahpf,ars_s,arsc,bbd,cytc,dsre,duf1858,fesor,fmdb,frha,ftrb,gpx_b,grx,gst,hesb_like,imp,merp,mert,msra_b,mucd,nadh_ox,pp_sp1,prx,prx_like,rhor,rnfb,rnfc,rsam,seld,soret,tdip,ugc,ugsc,uos_hp3,usha,yeee,di_b,dsba,dsbg,fdha,frhd,frx,grda,grdb,hdra,prdb
families_set.metazoa =  SEPHS2,DIO,SELENOE,FrnE,GPX,MsrA,SELENOF,SelKi,SELENOH,SELENOI,SELENOJ,SELENOK,SELENOL,SELENOM,SELENON,SELENOO,SELENOP,MSRB,SELENOS,SELENOU,TXNRD,SELENOT,SELENOW,AhpC
families_set.protist =    EhSEP2,Lmsel1,Sel1,Sel2,Sel3,Sel4,SelQ,SelTryp,MSP,Ostsp1,Ostsp2,Ostsp3
families_set.machinery  =  SEPHS2,SBP2,SecS,eEFsec,pstk,secp43
families_set.eukarya   =  metazoa,protist
families_set.se_traits   =  machinery,ybbb,yqeb,yqec

families_set.all = machinery,metazoa,protist,prokarya

"""
