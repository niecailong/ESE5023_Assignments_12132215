program Solar_elevation_angle

use Solar_hour_angle
use Declination_angle

implicit none

real(4), parameter :: pi = 3.14
real(4)            :: lat, lon, Z, LST, h, delta, SEA
integer(4)         :: day


lat = 22.542883
lon = 114.062996
Z = 8
LST = 10.533333
day = 364


call cal_declination_angle(day, delta)

call cal_solar_hour_angle(lon, Z, day, LST, h)


SEA = asin(sin(lat*pi/180)*sin(delta)+cos(lat*pi/180)*cos(delta)*cos(h*pi/180))*180/pi
print*, 'SEA = ', SEA

end program Solar_elevation_angle
