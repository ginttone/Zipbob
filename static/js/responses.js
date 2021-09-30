function getBotResponse(input) {
    //간단한 응답
    if (input == "안녕") {
        console.log("만나서 반가워요");
        return "만나서 반가워요!";
    } else if (input == "잘 있어") {
        console.log("즐거웠어요. 다음에 만나요!");
        return "즐거웠어요. 다음에 만나요!";
    } else if (input == "모각코") {
        console.log("오늘도 즐겁게 공부해봐요. 파이팅!");
        return "오늘도 즐겁게 공부해봐요. 파이팅!";
    } else if (input == "날씨") {
        console.log("요즘 너무 덥죠?");
        return "요즘 너무 덥죠?";
    } else {
        console.log("잘 이해하지 못했어요. 다른 이야기를 해볼까요?");
        return "잘 이해하지 못했어요. 다른 이야기를 해볼까요?";
    }
}