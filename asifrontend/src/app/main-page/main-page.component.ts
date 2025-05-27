import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ModelFormData } from './ModelFormData.model';

@Component({
  selector: 'app-main-page',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.css'
})
export class MainPageComponent {




positionList = ['Software Engineer', 'HR Specialist', 'Project Manager', 'Accountant'];
dateofHireList = ['2020-01-15', '2021-06-30', '2019-03-12', '2022-09-05'];
termReasonList = ['Resigned', 'Laid Off', 'Retired', 'Terminated for Cause'];
employmentStatusList = ['Full-Time', 'Part-Time', 'Contract', 'Intern'];
departmentList = ['IT', 'HR', 'Finance', 'Marketing', 'Operations'];
performanceScoreList = ['Exceeds Expectations', 'Meets Expectations', 'Below Expectations'];
engagementSurveyList = ['4.5', '3.8', '4.2', '3.0', '4.9'];
empSatisfactionList = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied'];
daysLateLast30List = ['0', '1', '2', '5', '10'];
absencesList = ['0', '1', '2', '3', '4', '5'];




  formData: ModelFormData = {
    Position: '',
    DateofHire: '',
    TermReason: '',
    EmploymentStatus: '',
    Department: '',
    PerformanceScore: '',
    EngagementSurvey: '',
    EmpSatisfaction: '',
    DaysLateLast30: '',
    Absences: ''
  };





  onSubmit() {
    console.log(this.formData);
  }




}
