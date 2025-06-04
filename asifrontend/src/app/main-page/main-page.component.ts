import { Component } from '@angular/core';
import { ModelFormData } from './ModelFormData.model';
import { ApiService } from '../ApiService';

@Component({
  selector: 'app-main-page',
  templateUrl: './main-page.component.html',
  styleUrl: './main-page.component.css'
})
export class MainPageComponent {

  constructor(private apiService: ApiService) {}

  departmentList = ['Admin Offices', 'Executive Office', 'IT/IS', 'Production', 'Sales', 'Software Engineering'];
  performanceScoreList = ['Exceeds', 'Fully Meets', 'Needs Improvement', 'PIP'];


  validationErrors = {
    departmentError: '',
    performanceScoreError: '',
    engagmentSurveyError: '',
    empSatisfactionError: '',
    daysLateLast30Error: '',
    absencesError: '',
    yearsAtCompanyError: ''
  };

  result: string = "";


  formData: ModelFormData = {
    department: '',
    performanceScore: '',
    engagmentSurvey: 0,
    empSatisfaction: 0,
    daysLateLast30: 0,
    absences: 0,
    yearsAtCompany: 0
  };


  onSubmit() {
    
    console.log(this.formData);

    var validationResult = this.fieldValidator(this.formData)

    if(validationResult){
     this.apiService.getPrediction(this.formData).subscribe({
      next: (data) => {
        this.result = data;
      },
      error: (err) => {
        console.error('Błąd podczas pobierania danych:', err);
      }

    });
  }
  }


  fieldValidator(data: ModelFormData){
    let isValid = true;

    this.validationErrors.departmentError= '',
    this.validationErrors.performanceScoreError= '',
    this.validationErrors.engagmentSurveyError = '';
    this.validationErrors.empSatisfactionError = '';
    this.validationErrors.daysLateLast30Error = '';
    this.validationErrors.absencesError = '';
    this.validationErrors.yearsAtCompanyError = '';

    if(data.engagmentSurvey > 5 || data.engagmentSurvey < 0){
      this.validationErrors.engagmentSurveyError = 'Wartość od 0 do 5';
      isValid = false;
      this.result = '';
    }

    if(data.empSatisfaction > 5 || data.empSatisfaction < 0){
      this.validationErrors.empSatisfactionError = 'Wartość od 0 do 5';
      isValid = false;
      this.result = '';
    }

    if(data.daysLateLast30 > 100 || data.daysLateLast30 < 0){
      this.validationErrors.daysLateLast30Error = 'Wartość od 0 do 100';
      isValid = false;
      this.result = '';
    }

    if(data.absences > 100 || data.absences < 0){
      this.validationErrors.absencesError = 'Wartość od 0 do 100';
      isValid = false;
      this.result = '';
    }


    if(data.yearsAtCompany > 100 || data.yearsAtCompany < 0){
      this.validationErrors.yearsAtCompanyError = 'Wartość od 0 do 100';
      isValid = false;
      this.result = '';
    }

    if(!data.department || data.department === ''){
      this.validationErrors.departmentError = 'Wybierz z listy';
      isValid = false;
      this.result = '';
    }

    if(!data.performanceScore || data.performanceScore === ''){
      this.validationErrors.performanceScoreError = 'Wybierz z listy';
      isValid = false;
      this.result = '';
    }

    return isValid;
  }

}
