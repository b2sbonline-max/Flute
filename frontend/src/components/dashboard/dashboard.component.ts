import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';
import { TableService } from '../../services/table.service';
import { User, TableRegistry } from '../../models/interfaces';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  currentUser: User | null = null;
  tables: TableRegistry[] = [];
  loading = false;
  error: string = '';

  constructor(
    private authService: AuthService,
    private tableService: TableService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.authService.currentUser$.subscribe(user => {
      this.currentUser = user;
    });
    this.loadTables();
  }

  loadTables(): void {
    this.loading = true;
    this.error = '';
    this.tableService.getTables().subscribe({
      next: (tables) => {
        this.tables = tables;
        this.loading = false;
      },
      error: (error) => {
        this.error = 'Failed to load tables';
        this.loading = false;
      }
    });
  }

  logout(): void {
    this.authService.logout();
    this.router.navigate(['/login']);
  }

  createTable(): void {
    this.router.navigate(['/create-table']);
  }

  openTable(table: TableRegistry): void {
    this.router.navigate(['/tables', table.table_name_en]);
  }

  deleteTable(table: TableRegistry): void {
    if (confirm(`Delete ${table.table_name_he}?`)) {
      this.tableService.deleteTable(table.table_name_en).subscribe({
        next: () => { this.loadTables(); },
        error: () => { this.error = 'Failed to delete'; }
      });
    }
  }
}
