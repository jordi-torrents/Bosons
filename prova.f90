program prova
  character(1024) :: filename
  real(8) :: t
  t=0.d0
  do i=1,11
    write(filename,"(A4,I4.4)") 'file', nint(t*1000)
    write(*,*) trim(filename)
    t=t+0.1d0
  end do
end program
