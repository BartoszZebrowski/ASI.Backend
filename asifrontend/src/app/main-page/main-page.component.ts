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
  };
  
  result: number | null = null;
  rangeOffset: number | null = null; 

formData: ModelFormData = {
  department: '',
  performanceScore: '',
  engagmentSurvey: null,
  empSatisfaction: null,
  daysLateLast30: null,
  absences: null,
  yearsAtCompany: null,
  specialProjectsCount: null
};


  onSubmit() {
    
    console.log(this.formData);

    var validationResult = this.OptionSelectValidator(this.formData)

    if(validationResult){
     this.apiService.getPrediction(this.formData).subscribe({
      next: (data) => {

        
        this.rangeOffset = Math.round((data * 0.15)/2);

        console.log("rangeOffset:   " + this.rangeOffset)
        console.log("data:   "+data)


        this.result = data
      },
      error: (err) => {
        console.error('Błąd podczas pobierania danych:', err);
      }

    });
  }
  }

  OptionSelectValidator(data: ModelFormData){
    let isValid = true;

    this.validationErrors.departmentError= '';
    this.validationErrors.performanceScoreError= '';


    if(!data.department || data.department === ''){
      this.validationErrors.departmentError = 'Wybierz z listy';
      isValid = false;
      this.result = 0;
    }

    if(!data.performanceScore || data.performanceScore === ''){
      this.validationErrors.performanceScoreError = 'Wybierz z listy';
      isValid = false;
      this.result = 0;
    }

    return isValid;
  }


  validateZeroFiveRange(data: ModelFormData){

    if(data.engagmentSurvey !== null){
      if (data.engagmentSurvey > 5) {
        data.engagmentSurvey = 5;
      } else if (data.engagmentSurvey < 0) {
        data.engagmentSurvey = 0;
      }
    }

    if(data.empSatisfaction !== null){
      if (data.empSatisfaction > 5) {
        data.empSatisfaction = 5;
      } else if (data.empSatisfaction < 0) {
        data.empSatisfaction = 0;
      }
    }

    if(data.daysLateLast30 !== null){
      if (data.daysLateLast30 > 100) {
        data.daysLateLast30 = 100;
      } else if (data.daysLateLast30 < 0) {
        data.daysLateLast30 = 0;
      }
    } 

    if(data.absences !== null){
      if (data.absences > 100) {
        data.absences = 100;
      } else if (data.absences < 0) {
        data.absences = 0;
      }
    }

    if(data.yearsAtCompany !== null){
      if (data.yearsAtCompany > 100) {
        data.yearsAtCompany = 100;
      } else if (data.yearsAtCompany < 0) {
        data.yearsAtCompany = 0;
      }
    }

      if(data.specialProjectsCount !== null){
        if (data.specialProjectsCount > 100) {
          data.specialProjectsCount = 100;
      } else if (data.specialProjectsCount < 0) {
        data.specialProjectsCount = 0;
      }
    }

  }
}
