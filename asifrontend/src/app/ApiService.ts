import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { ModelFormData } from './main-page/ModelFormData.model';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient) {}

  
  getPrediction(model: ModelFormData): Observable<number> {
    
    const url = 'http://192.168.1.41:8000/predict';
    let headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    return this.http.post<number>(url, model, {headers});

  }
}
