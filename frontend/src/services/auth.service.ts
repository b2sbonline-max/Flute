import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { environment } from '../environment';
import { User, LoginCredentials, AuthResponse } from '../models/interfaces';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = `${environment.apiUrl}/users`;
  private currentUserSubject = new BehaviorSubject<User | null>(null);
  public currentUser$ = this.currentUserSubject.asObservable();

  private tokenSubject = new BehaviorSubject<string | null>(null);
  public token$ = this.tokenSubject.asObservable();

  constructor(private http: HttpClient) {
    this.loadFromLocalStorage();
  }

  register(username: string, email: string, password: string, fullName?: string): Observable<User> {
    return this.http.post<User>(`${this.apiUrl}/register`, {
      username, email, password, full_name: fullName
    });
  }

  login(credentials: LoginCredentials): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.apiUrl}/login`, credentials).pipe(
      map(response => {
        localStorage.setItem(environment.tokenKey, response.access_token);
        localStorage.setItem('current_user', JSON.stringify(response.user));
        this.tokenSubject.next(response.access_token);
        this.currentUserSubject.next(response.user);
        return response;
      })
    );
  }

  logout(): void {
    localStorage.removeItem(environment.tokenKey);
    localStorage.removeItem('current_user');
    this.tokenSubject.next(null);
    this.currentUserSubject.next(null);
  }

  getCurrentUser(): User | null {
    return this.currentUserSubject.value;
  }

  getToken(): string | null {
    return this.tokenSubject.value;
  }

  isLoggedIn(): boolean {
    return !!this.getToken();
  }

  private loadFromLocalStorage(): void {
    const token = localStorage.getItem(environment.tokenKey);
    const user = localStorage.getItem('current_user');
    if (token) this.tokenSubject.next(token);
    if (user) this.currentUserSubject.next(JSON.parse(user));
  }
}
