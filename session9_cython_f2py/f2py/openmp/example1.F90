Subroutine dotprod(a,b,c)
    USE OMP_LIB
    Implicit None
    Real*8, Intent(InOut) :: a(:), b(:)
    Real*8, Intent(InOut)  :: c
    Integer :: i, n
    n = size(a)
    c = 0.0d0
    !$OMP PARALLEL DO PRIVATE(i) SHARED(a,b) REDUCTION(+:c)
    Do i = 1, n
        c = c+a(i)*b(i)
    EndDo
    !$OMP END PARALLEL DO
End Subroutine dotprod
