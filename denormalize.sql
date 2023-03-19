/***********************************************/
/* Denormalize tables from 'demo' to 'demods'  */
/***********************************************/

/* Denormalize the instructor_info table */

SELECT instructor_id,lname,fname,ssn,sex,active_status,start_date,specialty,
       addr_type,street1,street2,city,state,country
  FROM instructor JOIN instructor_info using(instructor_id)
             LEFT JOIN address         on instructor_id=inst_id; 
           
           
/* Denormalize the student_info table */

SELECT student_id,lname,fname,ssn,sex,email,
       addr_type,street1,street2,city,state,country
  FROM student LEFT JOIN student_email using(student_id)
               LEFT JOIN address       on student_id=stu_id;  
             
             
/* Denormalize the roster table */

select s.student_id,s.fname,s.lname,s.ssn,s.sex,
       c.session_id,co.course_id,co.description,co.price,
       i.instructor_id,i.fname,i.lname,i.ssn,i.sex 
  from class c join student s    on stu_ssn=s.ssn
               join course co    on c.course_id=co.course_id
               join instructor i on inst_ssn=i.ssn
UNION
select s.student_id,s.fname,s.lname,s.ssn,s.sex,
       null,null,null,null,
       null,null,null,null,null 
  from class c right join student s on stu_ssn=s.ssn 
 where c.course_id is null

UNION
select null,null,null,null,null,
       null,null,null,null,
       i.instructor_id,i.fname,i.lname,i.ssn,i.sex
  from class c right join instructor i on inst_ssn=i.ssn 
 where c.course_id is null

UNION
select null,null,null,null,null,
       null,co.course_id,co.description,co.price,
       null,null,null,null,null
  from class c right join course co on c.course_id=co.course_id 
 where c.course_id is null


