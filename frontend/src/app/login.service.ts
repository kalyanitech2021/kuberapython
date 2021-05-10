import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Login } from './login/login';

const loginUrl = "http://localhost:5000";

@Injectable({
  providedIn: 'root'
})

export class LoginService {

  input: string = "";

  login: Login = {
    user_id: "",
    password: ""
  }

  constructor(private http: HttpClient) { }

  create(user) {
    return this.http.post(loginUrl + "/login", user);
  }
}

  