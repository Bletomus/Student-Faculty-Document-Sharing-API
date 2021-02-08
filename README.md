## Student Faculty Document Sharing API
### [**Created by Leon**](https://bletomus.github.io/) **Pirate Utilities**

### Student Faculty-Document Sharing API

Student Faculty-Document Sharing API provides api calls that connect the [Student Faculty Document Sharing App](https://bletomus.github.io/Student_Faculty-Document-Sharing-App/) to the server and enable file sharing for the students and faculty.

- _Duration_ : December 2020 – January 2021 
- _Team Size_ : 1
- _Role Played_ : Developer and Tester
- _Skills_ : Flutter 
- _APP_ : [Student Faculty Document Sharing App](https://bletomus.github.io/Student_Faculty-Document-Sharing-App/)

## API calls

### Base URL

#### https//host/api/v1/students/

### APIS

#### validate_student/<int:person_id>

- Takes the student number set in a Get request and returns 200 status  code if the user is available or 404 otherwise

#### get_student_details/<int:person_id>

- Takes the student number set in a Get request and returns JSON containing the student's personal information.

#### set_up_database/

- Special Get call that innitializes the database and makes dummy input for testing.(Will be removed in the future)

#### get_Student_Takes/<int:person_id>

-  Takes the student number set in a Get request and returns JSON containing the student's classes which they are in.

#### get_Student_Scores/<int:person_id>

- Takes the student number set in a Get request and returns JSON containing the student's acores for the semester.

#### get_Courses/<int:person_id>

- Takes the student number set in a Get request and returns JSON containing the student's courses for the entirety of their study.

#### get_schedule/<int:person_id>

- Takes the student number set in a Get request and returns JSON containing the student's schedule for their classes.

### Base URL

#### https//host/api/v1/notifications/

### APIS

#### upload_file/<slug:person_id>/<int:sub_type>

- Takes an ObjectID of a user in the database and uploads a file that is attached in a MultiForm Post request.

#### get_faculty_notifications/<int:person_id>

- Takes the person number set in a Get request and returns JSON containing notifications specifically for the teacher.

#### get_student_notifications/<int:person_id>

- Takes the student number set in a Get request and returns JSON containing notifications specifically for the student.

#### get_Uploads/

- Post body with a special location string is sent to the server and the server will return a unique list of uploads correspoding to that location.

#### download_For_Notification_File/<objectid>

- Takes the ObjectID of a notification and returns an asscociated file  

#### download_file/<objectid>

- Takes the ObjectID of a upload and returns an asscociated file 

#### upload_file_in_note/<int:person_id>

- Takes the ObjectID of a user in the database as well as a MultiForm Post request containing the upload and dept of the uploader and uploads the file to the database. 

### Base URL

#### https//host/api/v1/teachers/

### APIS

#### validate_teacher/<int:person_id>

- Takes the person number set in a Get request and returns 200 status  code if the user is available or 404 otherwise

#### get_faculty_details/<int:person_id>

- Takes the person number set in a Get request and returns JSON file containing the teacher's information.

#### get_Teaches/<int:person_id>
- Takes the person number set in a Get request and returns JSON containing the teacher's classes which they are teaching.

## Contact Us
To view my other projects just follow this [link](https://bletomus.github.io/) or send me an email at leonkanyayi@yahoo.com

Logo made by [DesignEvo free logo creator]("https://www.designevo.com/)