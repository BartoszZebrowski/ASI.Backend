import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ModelFormData } from './main-page/ModelFormData.model';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {}

  
  getPrediction(model: ModelFormData): Observable<string> {
    
    const url = 'http://localhost:8000/predict';
    let headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<string>(url, model, {headers});

  }
}
