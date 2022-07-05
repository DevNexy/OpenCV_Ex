import matplotlib.pyplot as plt # 그래프그리기 라이브러리 임포트
import numpy as np

t = np.arange(0,1,0.001)    #샘플링 범위 및 개수
Hz = [1,2,10,100]   #주파수 예시
gs =[np.sin(2*np.pi*t*h)for h in Hz]    #sin 함수 계산

plt.figure(figsize=(10,5))
for i, g in enumerate(gs):
    plt.subplot(2,2,i+1), plt.plot(t, g)    #그래프 그리기
    plt.xlim(0,1),plt.ylim(-1,1)    #x,y 축 범위 지정
    plt.title("frequency: %3d Hz" % Hz[i])
plt.tight_layout()
plt.show()