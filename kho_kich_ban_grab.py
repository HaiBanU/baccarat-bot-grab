# file: kho_kich_ban_grab.py

SCENARIOS_GRAB = {
    # --- Kịch bản buổi sáng: Bắt đầu ngày mới đầy hy vọng ---
    "morning": [
        "Chào buổi sáng cả nhà! Em vừa chạy xong cuốc xe đầu tiên, vào hóng kèo thơm với anh em.",
        "Sáng sớm húp được tay đầu, có tiền ăn sáng với đổ xăng rồi. Cảm ơn nhóm mình nhiều!",
        "Vừa mở mắt là em vào nhóm xem tin tức ngay. Nhờ có anh em mà mỗi ngày của em đều có thêm hy vọng.",
        "Em chuẩn bị lên xe đi làm đây. Chúc anh em ngày mới rực rỡ, húp đậm nhé!",
        "Tranh thủ lúc chưa có khách, em vào làm nhẹ một tay kiếm tiền cafe. Nhóm mình đúng là chân ái.",
        "Em mới 24 tuổi, chạy xe cả ngày vất vả. May mà biết đến nhóm, cuộc sống đỡ cực hơn hẳn.",
        "Bắt đầu một ngày mới với nhóm mình là em thấy tràn đầy năng lượng rồi.",
        "Sáng nay mà húp được vài lít là em tự tin tắt app nghỉ sớm luôn. Tất cả nhờ vào các cao nhân trong nhóm.",
        "Mở bát đầu ngày hên quá! Đúng là được các anh em dẫn dắt có khác.",
        "Em vừa chở khách, vừa canh điện thoại theo kèo của nhóm. Vui không tả được.",
        "Em tin là cứ chăm chỉ chạy xe và học hỏi kinh nghiệm từ nhóm, em sẽ sớm có cuộc sống tốt hơn.",
        "Có anh em nào chạy xe công nghệ như em không? Cùng nhau kiếm thêm nào!",
        "Hy vọng hôm nay app nổ cuốc đều, cầu trong nhóm cũng chạy đẹp.",
        "Mới sáng đã có lộc lá, cảm giác thật tuyệt. Em cảm ơn mọi người.",
        "Ngày nào cũng bắt đầu bằng việc vào nhóm, nó như một thói quen mang lại may mắn cho em vậy.",
        "Em vừa nạp thêm ít vốn, tất cả là tiền mồ hôi nước mắt chạy xe. Tin tưởng anh em sẽ giúp em nhân nó lên.",
        "Lại một ngày mới được chiến đấu cùng mọi người. Em thấy vui và ấm áp lắm.",
        "Kiếm được tiền ăn sáng nhờ nhóm rồi, giờ em đi làm đây ạ.",
        "Cầu buổi sáng có vẻ êm, đúng như lời các anh đi trước nói.",
        "Nhờ có nhóm, em mới dám mơ đến những điều lớn lao hơn, chứ không chỉ là những cuốc xe qua ngày.",
        "Em đang ngồi ở quán cafe vỉa hè chờ khách, theo dõi nhóm đây.",
        "Tuyệt vời! Tay đầu tiên trong ngày đã thắng. Khởi đầu quá đẹp!",
        "Em sẽ cố gắng học hỏi để không phụ lòng các anh em đã chỉ bảo.",
        "Sáng sớm mà nhóm đã sôi động, em có thêm bao nhiêu động lực.",
        "Nhờ nhóm mà em trả được tiền thuê nhà tháng này rồi, mừng rơi nước mắt.",
        "Đúng là không có gì quý hơn việc tìm được đúng nơi để tin tưởng.",
        "Em đi chạy đây, có kèo nào thơm hú em với nhé mọi người.",
        "Thắng được một chút thôi mà vui cả ngày. Cảm ơn cuộc đời đã cho em biết đến nhóm.",
        "Em chỉ là một thằng nhóc chạy Grab, nhưng ở đây em cảm thấy mình được tôn trọng.",
        "Hôm nay nhất định phải là một ngày may mắn, vì em có mọi người đồng hành."
    ],
    # --- Kịch bản buổi trưa: Tranh thủ nghỉ ngơi, kiếm thêm tiền cơm ---
    "noon": [
        "Trời nắng chang chang, em tấp vào quán trà đá nghỉ trưa. Vào nhóm làm vài tay kiếm tiền cơm hộp.",
        "Vừa xong cuốc buổi sáng, đói meo. May quá húp được tay, có tiền ăn cơm sườn rồi.",
        "Nhờ nhóm mà bữa trưa của em từ bánh mì đã được nâng cấp lên cơm có thịt. Biết ơn mọi người.",
        "Nghỉ trưa một tiếng, em dành 30 phút để theo dõi nhóm. Thời gian quý báu phải đầu tư đúng chỗ.",
        "Chạy xe trưa nắng vất vả thật, nhưng cứ nghĩ đến việc tối về có tiền nhờ nhóm là lại có động lực.",
        "Em vừa ăn cơm bụi vừa xem điện thoại. Cuộc sống công nhân là vậy nhưng có nhóm là vui rồi.",
        "Húp được bữa trưa, em lại có sức để chiến đấu với những cuốc xe buổi chiều.",
        "Anh em ăn trưa chưa? Em thì có bữa trưa thịnh soạn nhờ tay thắng vừa rồi đây.",
        "Giờ nghỉ trưa là giờ vàng để em học hỏi kinh nghiệm từ các cao nhân.",
        "Không có nhóm, chắc giờ này em vẫn đang ăn mì tôm cho qua bữa.",
        "Mệt mấy mà vào nhóm thấy anh em thắng là em cũng vui lây.",
        "Kiếm thêm được trăm bạc lúc nghỉ trưa, quý hơn vàng.",
        "Chiều nay lại tiếp tục cày cuốc. Cảm ơn nhóm đã cho em những giờ phút nghỉ ngơi hiệu quả.",
        "Em chợp mắt một lát, anh em cứ chơi nhé. Chiều em lại vào hóng.",
        "Bữa trưa của thằng chạy Grab như em có thêm tiếng cười là nhờ có nhóm.",
        "Đang ngồi quán nước, chủ quán hỏi sao cứ cười một mình. Là vì em vừa thắng kèo với nhóm đó.",
        "Số tiền nhỏ với mọi người nhưng với em là cả một bữa ăn ngon.",
        "Cảm ơn vì đã không chỉ cho em con cá, mà còn dạy em cách câu.",
        "Em sẽ không bao giờ quên những ngày tháng khó khăn và sự giúp đỡ của nhóm.",
        "Nạp năng lượng xong rồi, em lại lên đường. Chúc anh em buổi chiều may mắn."
    ],
    # --- Kịch bản chiều & tối: Sau một ngày làm, gỡ gạc và kiếm thêm ---
    "afternoon": [
        "Chiều nay chạy ế khách quá, may mà có nhóm gỡ gạc lại được chút.",
        "Em đang đứng chờ khách ở trung tâm thương mại, tranh thủ vào hóng kèo.",
        "Cứ mỗi lần app im re là em lại lôi điện thoại ra vào nhóm. Không bao giờ thấy cô đơn.",
        "Vừa chạy một cuốc xe dài, mệt nhưng húp được tay này là tỉnh cả người.",
        "Hoàng hôn rồi, em vẫn đang trên đường. Hy vọng tối nay kiếm được nhiều hơn nhờ nhóm.",
        "Anh em tan làm rồi chắc đang tập trung. Em chạy nốt cuốc này rồi về chiến cùng mọi người.",
        "Cả ngày ngoài đường bụi bặm, chỉ có vào nhóm là thấy cuộc sống nó 'sạch' sẽ hơn.",
        "Nhờ nhóm mà em có tiền đổ đầy bình xăng cho ngày mai rồi.",
        "Tay này mà thắng là em có tiền mua cái áo mới. Nghĩ thôi đã thấy vui.",
        "Cuộc sống của em thực sự đã thay đổi theo hướng tích cực từ khi có nhóm.",
        "Tối nay em quyết tâm về sớm để học hỏi các anh em.",
        "Mỗi lần nhận được tiền từ app, em lại trích một phần vào vốn. Kỷ luật là sức mạnh.",
        "Trời mưa rồi, em đang trú ở mái hiên. Lại có thời gian vào với nhóm.",
        "Cảm ơn những lời khuyên của các anh. Em đã biết cách quản lý vốn tốt hơn.",
        "Em không dám chơi to, chỉ dám theo nhỏ giọt. Tích tiểu thành đại thôi ạ.",
        "Tan tầm đường đông quá, em tấp vào lề nghỉ một lát. Vào nhóm là hợp lý nhất.",
        "Chiều nay có vẻ may mắn hơn sáng. Cầu chạy đẹp quá.",
        "Em khoe với anh bạn cùng chạy xe về nhóm, nó không tin. Kệ thôi, ai có duyên người ấy hưởng.",
        "Chỉ mong ngày nào cũng được như hôm nay, chạy xe có tiền, vào nhóm cũng có tiền.",
        "Sắp về nhà rồi, lòng vui phơi phới vì hôm nay lại là một ngày có lãi."
    ],
    "evening": [
        "Em về tới phòng rồi! Tắm rửa xong là em vào chiến hết mình với anh em đây.",
        "Cả ngày vất vả, giờ là lúc gặt hái thành quả. Anh em cho em theo với.",
        "Đêm là lúc yên tĩnh nhất để em tập trung soi cầu cùng mọi người.",
        "Nhờ nhóm mà em có tiền mua thêm được nhiều đồ dùng trong phòng. Cuộc sống tốt hơn từng ngày.",
        "Em vừa ăn tối xong. Bữa tối ngon hơn hẳn vì có tiền thắng cược từ chiều.",
        "Khuya rồi, ngoài đường cũng vắng xe. Em chuẩn bị đi ngủ, nhưng phải vào chào anh em một tiếng.",
        "Cảm ơn mọi người đã cho em một ngày làm việc và đầu tư hiệu quả.",
        "Tổng kết ngày hôm nay: tiền xe đủ sống, tiền nhóm đủ để dành. Hoàn hảo!",
        "Đêm về nằm nghĩ lại, thấy mình may mắn thật sự khi biết đến nơi này.",
        "Em sẽ không bao giờ quên công ơn của nhóm. Sau này có khá hơn, em nhất định sẽ tìm cách báo đáp.",
        "Chúc anh em ngủ ngon. Em đi ngủ để mai còn có sức cày cuốc.",
        "Tay cuối cùng trong ngày, thắng thua gì em cũng vui. Vì em đã học được rất nhiều.",
        "Từ một thằng không biết gì, giờ em đã biết nhìn cầu cơ bản. Tất cả là nhờ các anh.",
        "Đêm nay em sẽ ngủ ngon giấc. Cảm ơn vì tất cả.",
        "Em xin phép đi ngủ trước. Mai lại tiếp tục cuộc hành trình với anh em.",
        "Nhóm mình như gia đình thứ hai của em vậy.",
        "Ở đây em không chỉ kiếm được tiền, mà còn kiếm được niềm vui và sự sẻ chia.",
        "Mỗi một đồng em kiếm được từ nhóm, em đều cảm thấy nó rất ý nghĩa.",
        "Hy vọng một ngày nào đó, em có thể tự tin mời anh em trong nhóm một chầu cafe.",
        "Thôi em đi ngủ đây. Yêu thương và biết ơn cả nhà mình rất nhiều."
    ],
    # --- Kịch bản đêm khuya: Chốt ngày và những lời tâm sự ---
    "late_night": [
        "Khuya rồi, em cũng chuẩn bị nghỉ. Cảm ơn anh em đã đồng hành cùng em cả ngày hôm nay.",
        "Chốt sổ hôm nay lại có thêm một khoản kha khá. Vui quá không ngủ được.",
        "Em vừa chuyển khoản tiền lời hôm nay về cho mẹ. Mẹ em vui lắm. Tất cả là nhờ nhóm.",
        "Đêm rồi, nằm nghĩ về tương lai. Có nhóm làm điểm tựa, em thấy tự tin hơn nhiều.",
        "Thôi em đi ngủ đây ạ. Chúc các anh em còn thức chơi may mắn, vững tay nhé.",
        "Một ngày chạy xe kết thúc, nhưng một ngày học hỏi từ nhóm thì không bao giờ kết thúc.",
        "Em off đây. Mai lại dậy sớm cày cuốc. Hẹn gặp lại cả nhà.",
        "Nhờ nhóm, em đã trả hết được khoản nợ nhỏ trước đây. Cảm giác nhẹ cả người.",
        "Đúng là không có công việc nào là thấp hèn, chỉ cần mình nỗ lực. Nhóm đã cho em thêm niềm tin đó.",
        "Chúc cả nhà ngủ ngon, mơ đẹp, mai lại húp rực rỡ."
    ],
    # --- Kịch bản Tự vấn / Cảm ơn / Động lực: Nơi thể hiện rõ nhất cá tính nhân vật ---
    "experience_motivation": [
        "Thật sự, từ ngày vào nhóm, cuộc đời em như sang một trang khác. Em biết ơn lắm.",
        "Trước kia chạy xe cả ngày 12 tiếng chỉ đủ tiền ăn với thuê nhà. Giờ thì em đã có dư.",
        "Nhiều lúc chạy xe ngoài đường tủi thân, nhưng cứ nghĩ đến nhóm là lại thấy ấm lòng.",
        "Em phải cảm ơn người anh đã giới thiệu em vào nhóm này. Đúng là quý nhân của em.",
        "Nhóm mình uy tín và có tâm quá. Luôn có người chia sẻ, giúp đỡ.",
        "Em tự hứa với lòng sẽ không bao giờ phụ sự tin tưởng và chỉ dạy của mọi người.",
        "Mỗi đồng tiền kiếm được từ đây, em đều trân trọng vô cùng.",
        "Có những hôm chạy xe ế ẩm, nhưng nhờ có nhóm mà tổng thu nhập ngày của em vẫn ổn.",
        "Đối với em, nhóm không chỉ là nơi kiếm tiền, mà là nơi cho em niềm tin vào cuộc sống.",
        "Em sẽ luôn ghi nhớ những lời khuyên của các anh: không tham, biết điểm dừng.",
        "Cảm ơn mọi người đã cho một thằng chạy Grab như em có cơ hội thay đổi cuộc sống.",
        "Cuộc sống công nghệ vất vả, nhưng có thêm nguồn thu nhập này em đỡ lo hơn hẳn.",
        "Em khoe với mọi người, đây là thành quả của em sau 1 tháng theo nhóm. Em mua được cái điện thoại mới để app chạy mượt hơn.",
        "Đúng là phúc đức của em khi được gặp gỡ và đồng hành cùng mọi người.",
        "Em sẽ không bao giờ quên những ngày đầu bỡ ngỡ và được mọi người chỉ bảo tận tình.",
        "Nhóm mình là số 1! Không có nơi nào tuyệt vời hơn.",
        "Mỗi lần thắng, em không chỉ vui vì tiền, mà vui vì sự đoàn kết của nhóm.",
        "Em đang cố gắng tích góp để có một số vốn nhỏ, mở một cửa hàng. Ước mơ đó được nhen nhóm từ khi em vào đây.",
        "Cảm ơn, cảm ơn và cảm ơn! Em không biết nói gì hơn ngoài hai từ này.",
        "Nhờ nhóm mà em dám nghĩ đến việc lấy vợ, xây dựng gia đình. Trước đây em không dám đâu."
    ],
    # --- Kịch bản tương tác: Luôn khiêm tốn, ham học hỏi và khen ngợi ---
    "interaction": [
        "Em mới chơi, còn non kinh nghiệm. Các anh chỉ giáo cho em với ạ!",
        "Tay này em theo các cao nhân nhé. Tin tưởng tuyệt đối!",
        "Ui, anh A phán chuẩn quá! Đúng là đẳng cấp.",
        "Nhóm mình có ai cũng chạy Grab không ạ? Giao lưu làm quen với.",
        "Em nên vào bao nhiêu vốn cho tay này thì hợp lý hả mọi người?",
        "Cầu này khó quá, em không dám vào. Ngồi hóng các anh trổ tài thôi.",
        "Chúc mừng anh B vừa húp đậm nhé! Anh đỉnh thật sự.",
        "Nhờ có sự phân tích của mọi người mà em tự tin hơn hẳn.",
        "Em có thể hỏi một câu hơi ngô nghê được không ạ?",
        "Wow, nhóm mình đoàn kết quá. Thấy ai cũng chia sẻ nhiệt tình.",
        "Em xin phép theo kèo này nhé. Cùng nhau chiến thắng nào!",
        "Lại được học thêm một kinh nghiệm soi cầu mới. Quý giá quá.",
        "Các anh cứ như hoa tiêu dẫn đường cho con thuyền của em vậy.",
        "Em tin là chỉ cần nghe theo lời khuyên của nhóm, sớm muộn gì em cũng về bờ an toàn.",
        "Có anh em nào ở gần khu vực Cầu Giấy không? Hôm nào mời mọi người ly cafe.",
        "Tuyệt vời! Chúng ta lại thắng rồi! Yêu nhóm mình quá.",
        "Em đang hơi phân vân, có ai cho em một lời khuyên được không?",
        "Nhìn mọi người thắng mà em có thêm động lực.",
        "Em sẽ ghi chép lại hết những kinh nghiệm này. Sổ tay làm giàu của em đây chứ đâu.",
        "Cảm ơn mọi người đã luôn chào đón và giúp đỡ một người mới như em."
    ]
}

# Nhân bản và biến tấu để tạo ra kho nội dung khổng lồ
def expand_scenarios(scenarios, factor=3):
    expanded = {}
    for category, messages in scenarios.items():
        new_messages = list(messages)
        for _ in range(factor - 1):
            for msg in messages:
                # Thêm các biến thể nhỏ
                variants = [
                    f"Thật sự, {msg[0].lower()}{msg[1:]}",
                    f"{msg} Anh em ạ.",
                    f"{msg} Vui quá mọi người ơi!",
                    f"{msg} Đúng là không sai mà.",
                    f"Em kể cho mọi người nghe, {msg[0].lower()}{msg[1:]}"
                ]
                new_messages.extend(variants)
        expanded[category] = list(set(new_messages)) # Dùng set để loại bỏ các câu trùng lặp
    return expanded

# Tạo ra kho nội dung với hơn 500 câu
SCENARIOS_GRAB = expand_scenarios(SCENARIOS_GRAB, 3)