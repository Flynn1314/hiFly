def merge_sort(arr):
    for i in range((len(arr)-1)//2,-1,-1):
        shift_down(arr,len(arr),i)
    for i in range(len(arr)):
        arr[0],arr[-1]=arr[-1],arr[0]
        shift_down(arr,i,0)


def shift_down(arr,n,k):
    while(2*k+1<n):
        j=2*k+1
        if arr[2*k+2]>arr[2*k+1]:
            j+=1
        if arr[k]>arr[j]:
            return
        else:
            arr[k],arr[j]=arr[j],arr[k]
        k=j
arr=[5,4,3,2,1,111]
merge_sort(arr)
print(arr)
def heap_sort(arr):
    #heapify�Ĺ��̣�heapify֮���������������һ������
    for i in range((len(arr)-1)//2,-1,-1):
        shift_down(arr,len(arr),i)
    #��̬�����Ĺ��̣����ν�����Ԫ�ط��������β��
    i = len(arr)-1
    while i>0:
    #ÿ��ֻ��Ҫ�ԶѶ�����һ��shiftdown����Ϊ�����ڽ������¶Ѷ��仯������Ϊ������
        arr[0],arr[i]=arr[i],arr[0]
        shift_down(arr,i,0)
        i -= 1
'''
n:��Ҫ�ָ���״̬������Ԫ�ظ���
k:Ҫshift����down��Ԫ��λ��
'''
def shift_down(arr,n,k):
    #ֻҪ�����ӣ���Ҫ���бȽ�
    while 2*k+1<n:
        j=2*k+1
        if j+1<n and arr[j+1]>arr[j]:
            j = j+1
        if arr[k]>arr[j]:
            break
        arr[k],arr[j]=arr[j],arr[k]
        k = j
