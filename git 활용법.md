jocoding > 이코테 가 로컬 저장소
3번째 repository -.git이 원격 저장소

로컬에 있는 문서를 수정

로컬 저장소 위치에서
1. git init
2. git add "파일명" - 깃이 그 파일을 지켜보게 함
3. git commit -m "메세지" - 수정사항 적기
4. git remote -v - 깃허브 remote 상태 보는 명령어
5. git remote add origin https://github.com/FutureMaker0/-.git - remote 과정 완료
- 5번 과정은 4번 입력 시 아무것도 안뜰 때 진행
6. git push -u origin master 
- 로컬 저장소에 있는 파일을 원격 저장소로 push

결국 add > commit > push 의 순서로 진행된다고 할 수 있다.


# 참고 사이트
- 개인 업로드
  - https://tychejin.tistory.com/357
- https://nevertrustbrutus.tistory.com/153

- 브랜치
  - https://velog.io/@chayezo/Git-Github-%EC%9B%90%EA%B2%A9-%EC%A0%80%EC%9E%A5%EC%86%8C-%EC%97%B0%EA%B2%B0-%EB%B0%8F-%EB%B8%8C%EB%9E%9C%EC%B9%98-add-commit-push-pull
  - https://victorydntmd.tistory.com/75

- 협업
  - https://coding-hwije.tistory.com/37
  - https://victorydntmd.tistory.com/91

- 에러
  - https://velog.io/@jenori_dev/githuberror-origin-%EB%A6%AC%EB%AA%A8%ED%8A%B8%EA%B0%80-%EC%9D%B4%EB%AF%B8-%EC%9E%88%EC%8A%B5%EB%8B%88%EB%8B%A4.-%EC%97%90%EB%9F%AC%ED%95%B4%EA%B2%B0

- 기타
  - https://hbase.tistory.com/16
  - https://tngusmiso.tistory.com/57 (gitmoji)
