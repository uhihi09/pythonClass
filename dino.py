import pygame
import sys
# 게임 초기화
pygame.init()
# 게임 창 제목
pygame.display.set_caption('Jumping dino')

MAX_WIDTH = 800
MAX_HEIGHT = 400

# 함수
def main():
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))  # 게임 창 크기를 설정 (가로 800, 세로 400)
    # 게임의 프레임 -> Clock 객체 생성
    fps = pygame.time.Clock()  # 게임 속도를 조절할 시계 생성
    # 이미지 로드, 위치
    imgDino1 = pygame.image.load('images/dino1.png')  # 공룡 이미지 불러오기 (다리 움직임용 첫 번째 이미지)
    dino_height = imgDino1.get_size()[1]
    dino_bottom = MAX_HEIGHT - dino_height
    # 공룡 위치
    dino_x = 50
    dino_y = dino_bottom

    imgTree = pygame.image.load('images/tree.png')  # 나무(장애물) 이미지 불러오기
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    # 공룡 최고치의 높이
    jump_top = 200
    is_bottom = True
    is_go_up = False

    # 공룡 다리가 움직임
    leg_swap = True
    # 공룡2 이미지
    imgDino2 = pygame.image.load('images/dino2.png')  # 공룡 이미지 불러오기 (다리 움직임용 두 번째 이미지)

    # 게임 무한 반복
    while True:
        # 스크린 하얀색
        screen.fill((255, 255, 255))
        # 공룡이 걷을 수 있게 함
        if leg_swap:
            screen.blit(imgDino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(imgDino2, (dino_x, dino_y))
            leg_swap = True
        # 이벤트
        for event in pygame.event.get():  # 사용자의 키보드나 창 닫기 등의 이벤트 처리
            # 창을 닫힘
            if event.type == pygame.QUIT:  # 창을 닫으면 게임 종료
                pygame.quit()
                sys.exit()
            # 키를 누르면 점프
            elif event.type == pygame.KEYDOWN:  # 키보드를 누르면 점프 시작 (공룡이 바닥에 있을 때만)
                if is_bottom:
                    is_go_up = True
                    is_bottom = False
         # 점프 했을때 y를 줄임/늘림
        if is_go_up:  # 점프 중이면 공룡을 위로 이동
            dino_y -= 10.0
        elif not is_go_up and not is_bottom:  # 점프가 끝나면 공룡을 아래로 이동
            dino_y += 10.0

        if is_go_up and dino_y <= jump_top:  # 점프 높이에 도달하면 다시 내려오게 설정
            is_go_up = False

        if not is_bottom and dino_y >= dino_bottom:  # 공룡이 바닥에 도달하면 상태 초기화
            is_bottom = True
            dino_y = dino_bottom
        # 나무 왼쪽 으로 이동
        screen.blit(imgDino1, (dino_x, dino_y))

        tree_x -= 12.0  # 나무를 왼쪽으로 이동시켜 공룡 쪽으로 다가오게 함
        if tree_x <= 0:  # 나무가 왼쪽 끝에 도달하면 다시 오른쪽으로 초기화
            tree_x = MAX_WIDTH

        screen.blit(imgTree, (tree_x, tree_y))

        # 충돌 감지
        # 공룡과 나무의 위치와 크기를 기준으로 각각의 Rect(사각형) 객체를 생성
        dino_rect = pygame.Rect(dino_x, dino_y, imgDino1.get_width(), imgDino1.get_height())
        tree_rect = pygame.Rect(tree_x, tree_y, imgTree.get_width(), imgTree.get_height())

        # 두 사각형(Rect)이 겹치는지(충돌하는지) 확인
        if dino_rect.colliderect(tree_rect):
            # 게임 오버 텍스트를 표시할 폰트 설정 (크기 80)
            font = pygame.font.SysFont(None, 80)
            # "Game Over!" 텍스트 생성 (빨간색)
            game_over_text = font.render("Game Over!", True, (255, 0, 0))
            # 텍스트를 화면 중앙 근처에 표시
            screen.blit(game_over_text, (MAX_WIDTH // 2 - 150, MAX_HEIGHT // 2 - 40))
            pygame.display.update()  # 텍스트를 화면에 즉시 보여줌
            pygame.time.wait(2000)  # 2초간 멈춤 (텍스트가 보이도록 대기)
            pygame.quit()  # pygame 종료
            sys.exit()     # 프로그램 완전히 종료
        pygame.display.update()  # 화면 업데이트 (변경 사항 보여주기)
        fps.tick(30)  # 초당 30번 화면을 그리도록 설정 (FPS)

# 함수 호출
if __name__ == '__main__':
    main()