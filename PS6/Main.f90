program Main
        implicit none

        integer::i,j,k,m,n,u
        real(4)::a(5,3),b(3,5),O(5,3)
        


        u=1 
        open(u,file="/work/ese-niecl/fortran_demo1/M.dat",status='old')
        
        do i=1,5
                read(u,*) (a(i,j),j=1,3)
                
        end do
        close(u)

        write(*,*)'M:'
        do i=1,5
        write(*,*)a(i,:)
        end do
    
         u=2
        open(u,file="/work/ese-niecl/fortran_demo1/N.dat",status='old')

        do i=1,3
                read(u,*) (b(i,j),j=1,5)

        end do
        close(u)
        write(*,*)'N:'
        do i=1,3
        write(*,*)b(i,:)
        end do

        
        u=3
        call Matrix_multip(a,b,O)
        open(u, file='MN.dat', status='replace') 
        !write(*,*)'M*N:'
        print *,'M*N'

        do i=1,5
        print *,O(i,:)
        write(3,'(f9.2,f9.2,f9.2)'),O(i,:)
        end do
        close(u)
       
end program Main

