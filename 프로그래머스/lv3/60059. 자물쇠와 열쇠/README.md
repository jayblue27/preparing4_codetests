# [level 3] 자물쇠와 열쇠 - 60059 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/60059) 

### 성능 요약

메모리: 10.2 MB, 시간: 6.36 ms

### 구분

코딩테스트 연습 > 2020 KAKAO BLIND RECRUITMENT

### 채점결과

<br/>정확성: 100.0<br/>합계: 100.0 / 100.0

### 문제 설명

<p style="user-select: auto;">고고학자인  <strong style="user-select: auto;">"튜브"</strong>는 고대 유적지에서 보물과 유적이 가득할 것으로 추정되는 비밀의 문을 발견하였습니다. 그런데 문을 열려고 살펴보니 특이한 형태의 <strong style="user-select: auto;">자물쇠</strong>로 잠겨 있었고 문 앞에는 특이한 형태의 <strong style="user-select: auto;">열쇠</strong>와 함께 자물쇠를 푸는 방법에 대해 다음과 같이 설명해 주는 종이가 발견되었습니다.</p>

<p style="user-select: auto;">잠겨있는 자물쇠는 격자 한 칸의 크기가  <strong style="user-select: auto;"><code style="user-select: auto;">1 x 1</code></strong>인  <strong style="user-select: auto;"><code style="user-select: auto;">N x N</code></strong> 크기의 정사각 격자 형태이고 특이한 모양의 열쇠는 <strong style="user-select: auto;"><code style="user-select: auto;">M x M</code></strong> 크기인 정사각 격자 형태로 되어 있습니다.</p>

<p style="user-select: auto;">자물쇠에는 홈이 파여 있고 열쇠 또한 홈과 돌기 부분이 있습니다. 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조입니다. 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.</p>

<p style="user-select: auto;">열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때, 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return 하도록 solution 함수를 완성해주세요.</p>

<h3 style="user-select: auto;">제한사항</h3>

<ul style="user-select: auto;">
<li style="user-select: auto;">key는 M x M(3 ≤ M ≤ 20, M은 자연수)크기 2차원 배열입니다.</li>
<li style="user-select: auto;">lock은 N x N(3 ≤ N ≤ 20, N은 자연수)크기 2차원 배열입니다.</li>
<li style="user-select: auto;">M은 항상 N 이하입니다.</li>
<li style="user-select: auto;">key와 lock의 원소는 0 또는 1로 이루어져 있습니다.

<ul style="user-select: auto;">
<li style="user-select: auto;">0은 홈 부분, 1은 돌기 부분을 나타냅니다.</li>
</ul></li>
</ul>

<hr style="user-select: auto;">

<h3 style="user-select: auto;">입출력 예</h3>
<table class="table" style="user-select: auto;">
        <thead style="user-select: auto;"><tr style="user-select: auto;">
<th style="user-select: auto;">key</th>
<th style="user-select: auto;">lock</th>
<th style="user-select: auto;">result</th>
</tr>
</thead>
        <tbody style="user-select: auto;"><tr style="user-select: auto;">
<td style="user-select: auto;">[[0, 0, 0], [1, 0, 0], [0, 1, 1]]</td>
<td style="user-select: auto;">[[1, 1, 1], [1, 1, 0], [1, 0, 1]]</td>
<td style="user-select: auto;">true</td>
</tr>
</tbody>
      </table>
<h3 style="user-select: auto;">입출력 예에 대한 설명</h3>

<p style="user-select: auto;"><img src="https://grepp-programmers.s3.amazonaws.com/files/production/469703690b/79f2f473-5d13-47b9-96e0-a10e17b7d49a.jpg" title="" alt="자물쇠.jpg" style="user-select: auto;"></p>

<p style="user-select: auto;">key를 시계 방향으로 90도 회전하고, 오른쪽으로 한 칸, 아래로 한 칸 이동하면 lock의 홈 부분을 정확히 모두 채울 수 있습니다.</p>


> 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges