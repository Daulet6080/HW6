import { Routes } from '@angular/router';

import { AboutUsComponent } from './about-us/about-us.component';
import { LoginComponent } from './login/login.component';

import { SignupComponent } from './signup/signup.component';
import { ProfileComponent } from './profile/profile.component';
import { ItemComponent } from './item/item.component';
import { ItemDetailsComponent } from './item-details/item-details.component';
import { HomePageComponent } from './home-page/home-page.component';
import { authGuard } from './services/auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: '/login', pathMatch: 'full' },

  { path: 'about', component: AboutUsComponent },
  { path: 'login', component: LoginComponent },
  { path: 'signup', component: SignupComponent },

  { path: 'profile', component: ProfileComponent, canActivate: [authGuard] },

  { path: 'items', component: ItemComponent },
  { path: 'items/:id', component: ItemDetailsComponent },

  { path: 'home', component: HomePageComponent },

  { path: '**', redirectTo: '/items' }
];
