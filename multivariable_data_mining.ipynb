/*=====================================================================*/
/* Multi-variable Data Mining models/predictions                       */
/*=====================================================================*/
/* Write a model that would predict the success (defined as grade>=90) */
/* of students based on their program and sex                          */
/* - First segment the raw data based on program and sex               */
/* - Next perform average on the various multi-variable combinations   */
/*=====================================================================*/
SELECT avg(Grad_M_seg)   as "Graduate M grade>90 prediction%", 
       avg(Grad_F_seg)   as "Graduate F grade>90 prediction%",
       avg(undGrad_M_seg)as "Undergrad M grade>90 rediction%",
       avg(undGrad_F_seg)as "Undergrad F grade>90 prediction%"
FROM (
    SELECT program, sex                           /*independent variables*/
        grade,                                    /*fact, or target variable*/
        case when program='graduate' and sex='M' then
            case when grade>=90 then 1 else 0 end 
        end as Grad_M_seg,  
        case when program='graduate' and sex='F' then
            case when grade>=90 then 1 else 0 end 
        end as Grad_F_seg,  
        case when program='undergraduate' and sex='M' then
            case when grade>=90 then 1 else 0 end 
        end as undGrad_M_seg,  
        case when program='undergraduate' and sex='F' then
            case when grade>=90 then 1 else 0 end 
        end as undGrad_F_seg 
    FROM grade natural join student
) raw_data
;

/*=================================================================*/
/* Write a model that would predict if there is instructor/student */
/* grade collusion based on sex                                    */
/*=================================================================*/
select round(avg(MM_seg),4) as "insM/stuM grade>90 prediction%",
       round(avg(MF_seg),4) as "insM/stuF grade>90 prediction%",
       round(avg(FM_seg),4) as "insF/stuM grade>90 prediction%",
       round(avg(FF_seg),4) as "insF/stuF grade>90 prediction%"
from (
    select i.sex as inst_sex, s.sex as stu_sex,       /*dimensions*/ 
           grade,                                     /*fact*/
           case when i.sex='M' and s.sex='M' then
               case when grade>90 then 1 else 0 end 
           end as MM_seg,  
           case when i.sex='M' and s.sex='F' then
               case when grade>90 then 1 else 0 end 
           end as MF_seg,  
           case when i.sex='F' and s.sex='M' then
               case when grade>90 then 1 else 0 end 
           end as FM_seg,  
           case when i.sex='F' and s.sex='F' then
               case when grade>90 then 1 else 0 end 
           end as FF_seg  
    from grade join student s    using(student_id)
               join instructor i using(instructor_id)
) raw_data
;

/*===============================================================*/
/* Write a model that would predict the probability of obtaining */
/* a grade >= 85 based on program and school_year                */
/*===============================================================*/
select round(avg(yr1),4) as "year1 grade>=85 prediction%", 
       round(avg(yr2),4) as "year2 grade>=85 prediction%",
       round(avg(yr3),4) as "year3 grade>=85 prediction%",
       round(avg(yr4),4) as "year4 grade>=85 prediction%",
       round(avg(yr5),4) as "yearG1 grade>=85 prediction%",
       round(avg(yr6),4) as "yearG2 grade>=85 prediction%"
from (
    select program, school_year, 
           grade,
           case when program='undergraduate' and school_year=1 then
               case when grade>=85 then 1 else 0 end 
           end as yr1,  
           case when program='undergraduate' and school_year=2 then
               case when grade>85 then 1 else 0 end 
           end as yr2,  
           case when program='undergraduate' and school_year=3 then
               case when grade>=85 then 1 else 0 end 
           end as yr3, 
           case when program='undergraduate' and school_year=4 then
               case when grade>85 then 1 else 0 end 
           end as yr4,  
           case when program='graduate' and school_year=1 then
               case when grade>=85 then 1 else 0 end 
           end as yr5,  
           case when program='graduate' and school_year=2 then
               case when grade>85 then 1 else 0 end 
           end as yr6  
    from grade natural join student 
) raw_data
;

/*===========================================================================*/
/* Write a model that would predict the probability of grade>=90 for student */
/* based on student sex and course department/concentration                  */
/*===========================================================================*/
select round(avg(IT_M), 4) as "M-IT  success prediction", 
       round(avg(IT_F), 4) as "F-IT  success prediction",
       round(avg(Web_M),4) as "M-Web success prediction",
       round(avg(Web_F),4) as "F-Web success prediction",
       round(avg(DB_M), 4) as "M-DB  success prediction",
       round(avg(DB_F), 4) as "F-DB  success prediction"
from (
    select department, sex 
           grade,
           case when department like 'Information%' and sex='M' then
               case when grade>=90 then 1 else 0 end 
           end as IT_M,  
           case when department like 'Information%' and sex='F' then
               case when grade>=90 then 1 else 0 end 
           end as IT_F,  
           case when department like 'Web%' and sex='M' then
               case when grade>=90 then 1 else 0 end 
           end as Web_M,  
           case when department like 'Web%' and sex='F' then
               case when grade>=90 then 1 else 0 end 
           end as Web_F,  
           case when department like 'Database%' and sex='M' then
               case when grade>=90 then 1 else 0 end 
           end as DB_M,  
           case when department like 'Database%' and sex='F' then
               case when grade>=90 then 1 else 0 end 
           end as DB_F  
    from grade natural join student
               natural join course  
) raw_data
;
