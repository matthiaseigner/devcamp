import pandas as pd
import numpy as np

# analyze data for teachers

# STATcube

# "Teaching Staff (Q)"
# "School year by Values, Sex, Age in 5 years group, Full-/Part-time and Schultyp (Ebene +1)"
# "Counting: Full-time equivalent, Number of teaching staff"
# "School year","Values","Sex","Age in 5 years group","Full-/Part-time","Schultyp (Ebene +1)","Number","Annotations",

# Symbol,Description
# "Q","STATcube � Statistical Database of STATISTICS AUSTRIA"
# "Teaching Staff",".) Origin of data and legal foundations Bundesgesetz �ber die Dokumentation im Bildungswesen (Bildungsdokumentationsgesetz) � 9 Abs. 2 Z 2 .) Update Annually. Next update planned for December 2018. Latest change of cube: [2019-11-27] .) Documentation Directorate Social Statistics, Science, Technology, Education. Cornelia Speckle, Tel. +43 (1) 71128-7681 cornelia.speckle@statistik.gv.at Other Metadata: http://www.statistik.at/web_en/statistics/PeopleSociety/education_culture/formal_education/teaching_staff/index.html"
# "School year","Reporting date: October of the school year (e.g. October 2016 for Data 2016/17)."
# "Full-/Part-time","Part-time teaching stuff are employed for less than 90% of the normal working hours of teaching staff in the same job."
# "School type","Classification of teaching staff: Classroom teachers are allocated to school types according to the number of classes in the particular school. Due to this classification, rounding differences in head-counts are possible. Teachers at schools for physical education and sports instructors training (intermediate schools for teacher training) and schools for the medical services are not included. Teachers at Vocational schools for agriculture and forestry for apprentices are included in schools and colleges for agriculture and forestry. Teachers at new secondary schools are assigned depending on school type of the new secondary school (""New secondary schools (general secondary schools)"" or academic secondary schools)."
# "Cumpulsory schools","Compulsory schools include Primary schools, new secondary schools (general secondary schools), special schools and pre-vocational schools."
# "Schools for Intermediate and Colleges for Higher Voc. Ed.","Schools and Colleges for vocational education include technical and crafts schools and colleges, schools and colleges of tourism, schools and colleges of business administration, schools and colleges of management and the service industries, schools and colleges for social professions, schools and colleges for agriculture and forestry and higher colleges for teacher training."
# "Teacher-training colleges (till 2015/16)","2016/17 change of school types: Higher colleges for teacher training are assigned at schools and colleges for vocational education."
# (c) Copyright Statistics Austria

teachers_file = './data/lehrerinnen.csv'
# teachers_lab_file = ?

if __name__ == "__main__": 
    teachers_df = pd.read_csv(teachers_file, dtype={
        "Annotations": str
        })
    # print(teachers_df)
    teachers_df[teachers_df['Number'] == '-'] = 0
    teachers_df['Number'] = teachers_df['Number'].astype(np.float64)

    teacher_fulltime_df = teachers_df[teachers_df['Values'] == 'Full-time equivalent']
    teacher_person_count_df = teachers_df[teachers_df['Values'] == 'Number of teaching staff']

    teachers_grouped_by_year_df = teachers_df.groupby(['School year', 'Sex', 'Values']).agg({
        'Number':'sum'})

    print(type(teachers_grouped_by_year_df))
    print(teachers_grouped_by_year_df) 

    # data_df = teachers_grouped_by_year_df[['Schoool year', 'Sex']]

    # print(data_df)

    # mask = (teachers_df['School year'] == '2017/18') & (teachers_df['Sex'] == 'male')
    # male_in_2017_18_df = len(teachers_df[mask])

    # print(male_in_2017_18_df)




# want to use copied code: 'print the count of exams per teacher' from lesson_1/e_10_main.py
#  semesters_df = ects_without_headers_df.groupby(['Prüfer/Prüferin']).agg({'Prüfer/Prüferin':'count', 'ECTS': 'sum', 'SSt.': 'sum', 'Note': 'mean'})
#  semesters_df = semesters_df.rename(columns={'Prüfer/Prüferin': 'count'})
#  print(semesters_df[semesters_df['count']>1].sort_values(by=['count'], ascending=False))