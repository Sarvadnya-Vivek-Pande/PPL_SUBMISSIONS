isinstitute(college_of_engineering_pune).


has_departments(college_of_engineering_pune, computer_science).
has_departments(college_of_engineering_pune, electronics_and_telecommunication).
has_departments(college_of_engineering_pune, instrumentation_and_control).
has_departments(college_of_engineering_pune, electrical).
has_departments(college_of_engineering_pune, mechanical).
has_departments(college_of_engineering_pune, civil).
has_departments(college_of_engineering_pune, production).
has_departments(college_of_engineering_pune, metallurgy).


has_year(BRANCH,first) :- has_departments(college_of_engineering_pune, BRANCH).
has_year(BRANCH,second) :- has_departments(college_of_engineering_pune, BRANCH).
has_year(BRANCH,third) :- has_departments(college_of_engineering_pune, BRANCH).
has_year(BRANCH,fourth) :- has_departments(college_of_engineering_pune, BRANCH).


has_division(BRANCH, YEAR, div1) :- has_departments(college_of_engineering_pune, BRANCH), has_year(BRANCH, YEAR).
has_division(BRANCH, YEAR, div2) :- has_departments(college_of_engineering_pune, BRANCH), has_year(BRANCH, YEAR).


offers_course(computer_science, second, dld).
offers_course(computer_science, second, dsa).
offers_course(computer_science, second, dsgt).
offers_course(computer_science, second, ppl).
offers_course(electronics_and_telecommunication, second, vlsi).
offers_course(electronics_and_telecommunication, second, dct).
offers_course(electronics_and_telecommunication, second, ocn).
offers_course(electronics_and_telecommunication, second, rns).
universal_course(odemc).


faculty_for(dld, X, jrw) :- has_division(computer_science, second, X).
faculty_for(dsa, Y, am_sk) :- has_division(computer_science, second, Y).
faculty_for(dsgt, Z, rs_vk) :- has_division(computer_science, second, Z).
faculty_for(ppl, W, sh_vk) :- has_division(computer_science, second, W).
faculty_for(vlsi, X, wrj) :- has_division(electronics_and_telecommunication, second, X).
faculty_for(dct, Y, ks_ma) :- has_division(electronics_and_telecommunication, second, Y).
faculty_for(ocn, Z, kv_sr) :- has_division(electronics_and_telecommunication, second, Z).
faculty_for(rns, W, kv_hs) :- has_division(electronics_and_telecommunication, second, W).
faculty_for(odemc,div1, gnd_mj).
faculty_for(odemc,div2, gnd_mj).

student(s1).
student(s2).
student(s3).
student(s4).
student(s5).
student(s6).
student(s7).
student(s8).
student(s9).
student(s10).
student(s11).
student(s12).


branch_and_year_of(s1, computer_science, second).
branch_and_year_of(s2, computer_science, second).
branch_and_year_of(s3, computer_science, second).
branch_and_year_of(s4, computer_science, second).
branch_and_year_of(s5, computer_science, second).
branch_and_year_of(s6, computer_science, second).
branch_and_year_of(s7, electronics_and_telecommunication, second).
branch_and_year_of(s8, electronics_and_telecommunication, second).
branch_and_year_of(s9, electronics_and_telecommunication, second).
branch_and_year_of(s10, electronics_and_telecommunication, second).
branch_and_year_of(s11, electronics_and_telecommunication, second).
branch_and_year_of(s12, electronics_and_telecommunication, second).


div_of(s1, div1).
div_of(s2, div1).
div_of(s3, div1).
div_of(s4, div2).
div_of(s5, div2).
div_of(s6, div2).
div_of(s7, div1).
div_of(s8, div1).
div_of(s9, div1).
div_of(s10, div2).
div_of(s11, div2).
div_of(s12, div2).



record_of(STUDENT, BRANCH, YEAR, DIV) :- student(STUDENT), branch_and_year_of(STUDENT, BRANCH, YEAR), div_of(STUDENT, DIV).
is_taught_by(STUDENT, SUBJECT, FACULTY) :-  (student(STUDENT), branch_and_year_of(STUDENT, BRANCH, YEAR), div_of(STUDENT, DIV), offers_course(BRANCH, YEAR, SUBJECT), faculty_for(SUBJECT, DIV, FACULTY)) ; (universal_course(SUBJECT), branch_and_year_of(STUDENT, BRANCH, YEAR), div_of(STUDENT, DIV), faculty_for(SUBJECT,DIV,FACULTY)).                                 
student_has_course(STUDENT, COURSE) :- (student(STUDENT), div_of(STUDENT, DIV), branch_and_year_of(STUDENT, BRANCH, YEAR), offers_course(BRANCH, YEAR, COURSE)) ; universal_course(COURSE).





