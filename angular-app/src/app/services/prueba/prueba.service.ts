// prueba.service.ts
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PruebaService {
  private dataUrl = environment.apiUrl + '/sensors/last-sensor-entry/1';

  constructor(private http: HttpClient) { }

  obtenerEstado(): Observable<any> {
    return this.http.get<any>(this.dataUrl);
    /*return of({
      "battery": {
        "status-data": "87.9 %"
      },
      "date": {
        "status-data": "Tue, 11 Jun 2024 16:55:59 GMT"
      },
      "humidity": {
        "status-data": "45.8 %"
      },
      "sensor_name": {
        "status-data": "sensor1"
      },
      "temperature": {
        "status-data": "25.5 \u00baC"
      }
    }
    );
    */
  }
}

