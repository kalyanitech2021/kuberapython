import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Login } from './login';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  
  show:boolean = true;

  currentUser: any;

  login: Login = {
    user_id: "",
    password: ""
  }

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private loginService: LoginService) {}

    public input: string = "";

    public onInput(a_oEvent): void {
    this.input = a_oEvent.currentTarget.value;
    this.loginService.input = a_oEvent.currentTarget.value;
  }

  ngOnInit(): void {
  }

  loginUser() {
    this.show = !this.show;

      const user = {
        user_id: this.login.user_id,
        password: this.login.password
      };
  
      console.log("<loginUser>: request is -- ", user);
  
      this.loginService.create(user)
        .subscribe(
          response => {
            this.currentUser = response;
            console.log("<loginUser>: response is -- ", response);
            if (this.currentUser.status === 401) {
              window.alert("Username or Password is incorrect!");
              this.router.navigate(['/login']);
            }
            else
              this.router.navigate(['/portfolio/' + this.input]);
          });
          error => {
            console.log(error);
          };
  }

  registerUser() {
    this.show = !this.show;    
    this.router.navigate(['/register']);
  }
}