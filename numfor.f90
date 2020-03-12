subroutine verlet_steps(r, v, F, t, n, steps, k, g, dt)
  integer :: n, steps, l
  real(8), dimension(n,2) :: r, v, F, F_new
  real(8) :: t, k, g, dt, d2
  real(8), dimension(2) :: dif, force_ij
  !f2py intent(inout) t
  do l=1,steps
    r = r+v*dt+F*0.5d0*dt**2
    F_new=0.d0
    do i=1,n
      F_new(i,:)=F_new(i,:)-k*r(i,:)
      do j=i+1,n
        dif = r(j,:) - r(i,:)
        d2=dif(1)*dif(1)+dif(2)*dif(2)
        force_ij = -2.d0*g*dif/(d2*d2)
        F_new(i,:)=F_new(i,:)+force_ij
        F_new(j,:)=F_new(j,:)-force_ij
      end do
    end do
    v = v + (F+F_new)*0.5d0*dt
    F=F_new
  end do
  t = t + dt*dble(steps)
end subroutine

subroutine forces(r, F, n, k, g)
  integer :: n
  real(8), dimension(n,2) :: r, F
  real(8), dimension(2)   :: dif, force_ij
  real(8) :: k, g, d2
  F=0.d0
  do i=1,n
    F(i,:)=F(i,:)-k*r(i,:)
    do j=i+1,n
      dif = r(j,:) - r(i,:)
      d2=dif(1)*dif(1)+dif(2)*dif(2)
      force_ij = -2.d0*g*dif/(d2*d2)
      F(i,:)=F(i,:)+force_ij
      F(j,:)=F(j,:)-force_ij
    end do
  end do
end subroutine

subroutine mesure(r, v, n, k, g, E_int, E_ho, E_kin)
  integer :: n, i, j
  real(8), dimension(n,2) :: r, v
  real(8) :: E_int, E_ho, E_kin, k, g
  real(8), dimension(2) :: dif
  !f2py intent(out) E_int, E_ho, E_kin
  E_int=0.d0
  E_ho=0.d0
  do i=1,n
    E_ho=E_ho+0.5d0*k*(r(i,1)*r(i,1) + r(i,2)*r(i,2))
    do j=i+1,n
      dif = r(j,:) - r(i,:)
      E_int=E_int+g/(dif(1)*dif(1)+dif(2)*dif(2))
    end do
  end do
  E_int=E_int/dble(n)
  E_ho=E_ho/dble(n)
  E_kin=0.5d0*sum(v*v)/dble(n)
end subroutine

subroutine verlet_steps_th(r, v, F, t, n, steps, k, g, dt, th)
  integer :: n, steps, l
  real(8), dimension(n,2) :: r, v, F
  real(8) :: t, k, g, dt, d2, th, th2
  real(8), dimension(2) :: dif, force_ij
  !f2py intent(inout) t
  th2 = th*th
  do l=1,steps
    r = r+v*dt+F*0.5d0*dt**2
    v = v + F*0.5d0*dt
    F=0.d0
    do i=1,n
      F(i,:)=F(i,:)-k*r(i,:)
      do j=i+1,n
        dif = r(j,:) - r(i,:)
        d2=dif(1)*dif(1)+dif(2)*dif(2)
        if (d2<th2) then
          force_ij = -2.d0*g*dif/(d2*d2)
          F(i,:)=F(i,:)+force_ij
          F(j,:)=F(j,:)-force_ij
        end if
      end do
    end do
    v = v + F*0.5d0*dt
  end do
  t = t + dt*dble(steps)
end subroutine

subroutine forces_th(r, F, n, k, g, th)
  integer :: n
  real(8), dimension(n,2) :: r, F
  real(8), dimension(2)   :: dif, force_ij
  real(8) :: k, g, d2, th, th2
  th2 = th*th
  F=0.d0
  do i=1,n
    F(i,:)=F(i,:)-k*r(i,:)
    do j=i+1,n
      dif = r(j,:) - r(i,:)
      d2=dif(1)*dif(1)+dif(2)*dif(2)
      if (d2<th2) then
        force_ij = -2.d0*g*dif/(d2*d2)
        F(i,:)=F(i,:)+force_ij
        F(j,:)=F(j,:)-force_ij
      end if
    end do
  end do
end subroutine

subroutine mesure_th(r, v, n, k, g, E_int, E_ho, E_kin, th)
  integer :: n, i, j
  real(8), dimension(n,2) :: r, v
  real(8) :: E_int, E_ho, E_kin, k, g, th, d2, E_cut
  real(8), dimension(2) :: dif
  !f2py intent(out) E_int, E_ho, E_kin
  E_cut = g/(th*th)
  E_int=0.d0
  E_ho=0.d0
  do i=1,n
    E_ho=E_ho+0.5d0*k*(r(i,1)*r(i,1) + r(i,2)*r(i,2))
    do j=i+1,n
      dif = r(j,:) - r(i,:)
      d2 = dif(1)*dif(1)+dif(2)*dif(2)
      if (d2<(th**2)) then
        E_int=E_int+g/d2-E_cut
      end if
    end do
  end do
  E_int=E_int/dble(n)
  E_ho=E_ho/dble(n)
  E_kin=0.5d0*sum(v*v)/dble(n)
end subroutine

subroutine calmdown(r, v, F, n, steps, g, dt, th, eps)
  integer :: n, steps, l
  real(8), dimension(n,2) :: r, v, F, F_new
  real(8) :: g, dt, d2, th, eps
  real(8), dimension(2) :: dif, force_ij
  do l=1,steps
    r = r+v*dt+F*0.5d0*dt**2
    F_new=0.d0
    do i=1,n
      do j=i+1,n
        dif = r(j,:) - r(i,:)
        d2=dif(1)*dif(1)+dif(2)*dif(2)+eps
        if (d2<th*th) then
          force_ij = -2.d0*g*dif/(d2*d2)
          F_new(i,:)=F_new(i,:)+force_ij
          F_new(j,:)=F_new(j,:)-force_ij
        end if
      end do
    end do
    v = v + (F+F_new)*0.5*dt
    F=F_new
  end do
end subroutine
