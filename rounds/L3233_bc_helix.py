import numpy as np, itertools
exec(open('/home/claude/geom/e8.py').read().split("# --- E8 -> 4D")[0].split("# --- 600-cell")[1].join(["phi=(1+5**.5)/2\nimport itertools\n",""]) if False else "")
phi=(1+5**.5)/2
# 3D Boerdijk-Coxeter helix: each new vertex = reflection of the vertex 3 back through the plane... use: v_{n+1} = 2*centroid(v_{n-2},v_{n-1},v_n) ... reflect v_{n-3} through face (v_{n-2},v_{n-1},v_n)
def reflect(p,a,b,c):
    n=np.cross(b-a,c-a); n/=np.linalg.norm(n); return p-2*np.dot(p-a,n)*n
v=[np.array([0,0,0.]),np.array([1,0,0.]),np.array([.5,3**.5/2,0]),np.array([.5,3**.5/6,(2/3)**.5])]
for _ in range(60): v.append(reflect(v[-4],v[-3],v[-2],v[-1]))
V=np.array(v)
# fit axis by PCA of centroids of tetrahedra
Cn=np.array([V[i:i+4].mean(0) for i in range(len(V)-3)]); c0=Cn.mean(0); ax=np.linalg.svd(Cn-c0)[2][0]
# rotation per vertex about axis
def proj(x): y=x-c0; return y-np.dot(y,ax)*ax
angs=[]
for i in range(10,50):
    a,b=proj(V[i]),proj(V[i+1]); ang=np.degrees(np.arctan2(np.dot(np.cross(a,b),ax),np.dot(a,b))); angs.append(ang)
rot=abs(np.mean(angs)); rise=abs(np.mean([np.dot(V[i+1]-V[i],ax) for i in range(10,50)]))
print("BC helix (unit edge): rotation per vertex %.4f deg, vertices per turn %.4f, rise per vertex %.4f"%(rot,360/rot,rise))
print("  check: arccos(-2/3) = %.4f deg; 360/(360-2*... ) not assumed"%np.degrees(np.arccos(-2/3)))
# 4D: tetrahelix rings inside the 600-cell
V4=[]
for i in range(4):
    for s in (1,-1): x=np.zeros(4); x[i]=s; V4.append(x)
for s in itertools.product((0.5,-0.5),repeat=4): V4.append(np.array(s))
base=[phi/2,0.5,1/(2*phi),0]
evens=[p for p in itertools.permutations(range(4)) if sum(1 for a in range(4) for b in range(a+1,4) if p[a]>p[b])%2==0]
for p in evens:
    for s in itertools.product((1,-1),repeat=3):
        x=np.zeros(4); vals=[base[0]*s[0],base[1]*s[1],base[2]*s[2],0]
        for k in range(4): x[p[k]]=vals[k]
        V4.append(x)
V4=np.unique(np.round(np.array(V4),9),axis=0); D=np.linalg.norm(V4[:,None]-V4[None],axis=2); A=np.isclose(D,1/phi)
def ring(i,j,k,l):
    ch=[i,j,k,l]
    for step in range(200):
        a,b,c=ch[-3],ch[-2],ch[-1]
        cand=[x for x in np.where(A[a]&A[b]&A[c])[0] if x!=ch[-4]]
        if len(cand)!=1: return None
        ch.append(cand[0])
        if ch[-4:]==ch[:4]: return len(ch)-4
    return None
# take one tetrahedral cell and grow its helix
i=0; j=np.where(A[i])[0][0]; k=[x for x in np.where(A[i]&A[j])[0]][0]; l=[x for x in np.where(A[i]&A[j]&A[k])[0]][0]
L=ring(i,j,k,l); print("600-cell: a face-to-face chain of tetrahedra closes after %s vertices (= %s tetrahedra)"%(L,L))
# how many disjoint rings partition the 600 cells? count distinct rings over all cells
cells=set()
for i in range(len(V4)):
    for j in np.where(A[i])[0]:
        for k in np.where(A[i]&A[j])[0]:
            for l in np.where(A[i]&A[j]&A[k])[0]:
                cells.add(tuple(sorted((i,j,k,l))))
print("cells",len(cells))
