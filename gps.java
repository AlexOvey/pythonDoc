 package org.renpy.android;

//import java.util.ArrayList;
//import java.util.List;

import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.content.Context;
import android.os.Bundle;
import android.os.Looper;
import java.lang.Thread;
import android.app.Activity;

public class KivyGps {
    LocationManager lm;
    Thread gpsThread;
    public long minDistance = 1;
    public int  minTime = 1000;


   static class KivyLocationListener implements LocationListener {

    public Location lastLocation = new Location("Other");
    //private List<LocationListener> listeners = new ArrayList<LocationListener>();

    public void onLocationChanged(Location location) {
        // TODO Auto-generated method stub
        lastLocation = location;
        //updateListeners(location);
    }

    public void onProviderDisabled(String provider) {
        // TODO Auto-generated method stub
    }

    public void onProviderEnabled(String provider) {
        // TODO Auto-generated method stub
    }

    public void onStatusChanged(String provider, int status, Bundle extras) {
        // TODO Auto-generated method stub
    }

        // TODO Auto-generated method stub
        return lastLocation;
    }

    }

    static public KivyLocationListener locationListener = new KivyLocationListener();
    public Thread init(final Activity currActivity) {

        gpsThread = new Thread( new Runnable() {

          public void run() {
            try {
                Looper.prepare();
                 lm = (LocationManager) currActivity.getSystemService( Context.LOCATION_SERVICE );
                 lm.requestLocationUpdates( LocationManager.GPS_PROVIDER, minTime, minDistance, locationListener );
                 Looper.loop();
                  }
            catch ( Exception e ) {
                e.printStackTrace();
            }
          }

        } );
        return gpsThread;    
    }
    //gpsThread.start();

}

/* code from here in written in python */
from jnius import autoclass

LocationListener = autoclass('android.location.LocationListener')
LocationManager = autoclass('android.location.LocationManager')
LocationProvider = autoclass('android.location.LocationProvider')
Location = autoclass('android.location.Location')
Looper = autoclass('android.os.Looper')
Context = autoclass('android.content.Context')
KivyGps = autoclass('org.renpy.android.KivyGps')

currentActivity = cast('android.app.Activity', PythonActivity.mActivity)
lm = currentActivity.getSystemService( Context.LOCATION_SERVICE)
if lm.isProviderEnabled( LocationManager.GPS_PROVIDER ):
    print 'CON GPS'

else:
    print 'SIN GPS'


lps = lm.getAllProviders()
for lp in lps.toArray():
    print lp
#Arreglar problema de derechos ACCESS_FINE_LOCATION en Kivy Launcher
lp = lm.getProvider('gps')

ll = KivyGps.locationListener
kgps = KivyGps()
gpsThread = kgps.init( currentActivity )
gpsThread.start()

loc = ll.getCurrentLocation()
if loc:
    print loc.getLatitude()
    print loc.getLongitude()