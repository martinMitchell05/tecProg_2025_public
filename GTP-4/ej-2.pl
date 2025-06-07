padre(leoncio, alberto).
padre(leoncio, geronimo).
padre(alberto, juan).
padre(alberto, luis).
padre(geronimo, luisa).
hermano(A, B) :- padre(P, A), padre(P, B), A \= B.
nieto(A, B) :- padre(P, A), padre(B, P).

/* ¿Cómo consultaría si Alberto es padre de Luis? --> padre(alberto,luis). */

/* ¿Cómo consultaría si Luis es padre de Alberto? --> padre(luis,alberto). */

/* ¿Cómo consultaría quién es hermano de Luis? --> hermano(Hermano,luis). */ 

/* ¿Cómo consultaría de quién es nieto Luisa? --> nieto(luisa,Abuelo). */

/* ¿Cómo consultaría quién es nieto de quién? --> nieto(Nieto,Abuelo). */