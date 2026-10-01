import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../environment';
import { TableRegistry, Field, CreateTableRequest, MessageResponse } from '../models/interfaces';

@Injectable({
  providedIn: 'root'
})
export class TableService {
  private apiUrl = `${environment.apiUrl}/tables`;

  constructor(private http: HttpClient) { }

  getTables(): Observable<TableRegistry[]> {
    return this.http.get<TableRegistry[]>(this.apiUrl);
  }

  getTable(tableName: string): Observable<TableRegistry> {
    return this.http.get<TableRegistry>(`${this.apiUrl}/${tableName}`);
  }

  createTable(table: CreateTableRequest): Observable<TableRegistry> {
    return this.http.post<TableRegistry>(this.apiUrl, table);
  }

  updateTable(tableName: string, tableNameHe: string): Observable<TableRegistry> {
    return this.http.put<TableRegistry>(`${this.apiUrl}/${tableName}`, { table_name_he: tableNameHe });
  }

  deleteTable(tableName: string): Observable<MessageResponse> {
    return this.http.delete<MessageResponse>(`${this.apiUrl}/${tableName}`);
  }

  getFields(tableName: string): Observable<Field[]> {
    return this.http.get<Field[]>(`${this.apiUrl}/${tableName}/fields`);
  }
}
