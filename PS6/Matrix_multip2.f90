subroutine Matrix_multip(a,b,O)
                implicit none
                integer::i,j,k
                real(4)::r
                real,dimension(5,3),intent(in)::a
                real,dimension(3,5),intent(in)::b
                real,dimension(5,5),intent(out)::O      
        !M * N
                       
                        do j=1,5
                        
                                do k=1,3
                                        r=(a(j,k) * b(k,j))
                                O(j,k)=r
                                end do
                        end do
               
        end subroutine  Matrix_multip
