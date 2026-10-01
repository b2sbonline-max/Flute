import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environment';
import { DataResponse, MessageResponse } from '../models/interfaces';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  private apiUrl = `${environment.apiUrl}/tables`;

  constructor(private http: HttpClient) { }

  getTableData(tableName: string): Observable<DataResponse> {
    return this.http.get<DataResponse>(`${this.apiUrl}/${tableName}/data`);
  }

  addRow(tableName: string, data: any): Observable<MessageResponse> {
    return this.http.post<MessageResponse>(`${this.apiUrl}/${tableName}/data`, data);
  }

  updateRow(tableName: string, rowId: number, data: any): Observable<MessageResponse> {
    return this.http.put<MessageResponse>(`${this.apiUrl}/${tableName}/data/${rowId}`, data);
  }

  deleteRow(tableName: string, rowId: number): Observable<MessageResponse> {
    return this.http.delete<MessageResponse>(`${this.apiUrl}/${tableName}/data/${rowId}`);
  }
}
