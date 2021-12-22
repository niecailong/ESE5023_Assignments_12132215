module Solar_hour_angle

contains

  subroutine cal_solar_hour_angle(lon,Z,day,LST,h)

    implicit none

    real(4), parameter     :: pi = 3.14
    real(4), intent(in)    :: lon, Z, LST                  
    integer(4), intent(in) :: day                            
    real(4), intent(out)   :: h                               
    real(4)                :: y, EoT, LST_crt    
     



    
    y = 2*pi/365*(day-1+(LST-12)/24)

    
    EoT = 229.18*(0.000075+0.001868*cos(y)-0.032077*sin(y)-0.014615*cos(2*y)-0.040849*sin(2*y))
    
    LST_crt = LST + (EoT + 4*(lon - 15*Z))/60

    h = 15*(LST_crt - 12)
    print*, 'h = ', h

  end subroutine cal_solar_hour_angle

end module Solar_hour_angle

