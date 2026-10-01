export interface User {
  id: number;
  username: string;
  email: string;
  full_name?: string;
  is_active: boolean;
  created_at: string;
  last_login?: string;
}

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface Field {
  id: number;
  table_name_en: string;
  field_name_he: string;
  field_name_en: string;
  field_type: 'varchar' | 'integer' | 'date' | 'boolean' | 'decimal';
  field_position?: number;
  created_at: string;
}

export interface TableRegistry {
  id: number;
  table_name_en: string;
  table_name_he: string;
  created_by: number;
  created_at: string;
  updated_at: string;
  fields: Field[];
}

export interface CreateTableRequest {
  table_name_en: string;
  table_name_he: string;
  fields: CreateFieldRequest[];
}

export interface CreateFieldRequest {
  field_name_he: string;
  field_name_en: string;
  field_type: 'varchar' | 'integer' | 'date' | 'boolean' | 'decimal';
  field_position?: number;
}

export interface DataRow {
  id: number;
  [key: string]: any;
}

export interface DataResponse {
  data: DataRow[];
  count: number;
}

export interface MessageResponse {
  message: string;
  success: boolean;
}

export interface ErrorResponse {
  detail: string;
  status_code?: number;
}
