import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Register } from './register/register';

const usersUrl = "http://localhost:5000/users";

@Injectable({
  providedIn: 'root'
})
export class RegisterService {

  register: Register = {
    _id: "",
    user_id: "",
    password: "",
    firstname: "",
    lastname: ""
  }

  constructor(private http: HttpClient) { }

  create(users) {
    return this.http.post(usersUrl, users);
  } 
}