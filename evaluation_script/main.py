import random
from zhipuai import ZhipuAI
API_KEY = "0c9745f6e0254f41818839057a62025b.EZ6Cq8FgHRPo91fk"

import json

def compute_iou(box1, box2):
    """
    计算两个边界框的IOU（Intersection over Union）
    :param box1: 第一个边界框 [[x1, y1], [x2, y2]]
    :param box2: 第二个边界框 [[x1, y1], [x2, y2]]
    :return: IOU值
    """
    # 标准化边界框坐标（确保左上角和右下角）
    x1s = [min(p[0] for p in box1), min(p[0] for p in box2)]
    x2s = [max(p[0] for p in box1), max(p[0] for p in box2)]
    y1s = [min(p[1] for p in box1), min(p[1] for p in box2)]
    y2s = [max(p[1] for p in box1), max(p[1] for p in box2)]

    # 获取交集坐标
    inter_x1 = max(x1s[0], x1s[1])
    inter_y1 = max(y1s[0], y1s[1])
    inter_x2 = min(x2s[0], x2s[1])
    inter_y2 = min(y2s[0], y2s[1])

    # 计算交集面积
    inter_width = max(0, inter_x2 - inter_x1)
    inter_height = max(0, inter_y2 - inter_y1)
    inter_area = inter_width * inter_height

    # 计算各自面积
    area1 = (x2s[0] - x1s[0]) * (y2s[0] - y1s[0])
    area2 = (x2s[1] - x1s[1]) * (y2s[1] - y1s[1])

    # 计算并集面积
    union_area = area1 + area2 - inter_area

    # 计算IOU
    return inter_area / union_area if union_area > 0 else 0.0
    
def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
    print("Starting Evaluation.....")
    """
    Evaluates the submission for a particular challenge phase and returns score
    Arguments:

        `test_annotations_file`: Path to test_annotation_file on the server
        `user_submission_file`: Path to file submitted by the user
        `phase_codename`: Phase to which submission is made

        `**kwargs`: keyword arguments that contains additional submission
        metadata that challenge hosts can use to send slack notification.
        You can access the submission metadata
        with kwargs['submission_metadata']

        Example: A sample submission metadata can be accessed like this:
        >>> print(kwargs['submission_metadata'])
        {
            'status': u'running',
            'when_made_public': None,
            'participant_team': 5,
            'input_file': 'https://abc.xyz/path/to/submission/file.json',
            'execution_time': u'123',
            'publication_url': u'ABC',
            'challenge_phase': 1,
            'created_by': u'ABC',
            'stdout_file': 'https://abc.xyz/path/to/stdout/file.json',
            'method_name': u'Test',
            'stderr_file': 'https://abc.xyz/path/to/stderr/file.json',
            'participant_team_name': u'Test Team',
            'project_url': u'http://foo.bar',
            'method_description': u'ABC',
            'is_public': False,
            'submission_result_file': 'https://abc.xyz/path/result/file.json',
            'id': 123,
            'submitted_at': u'2017-03-20T19:22:03.880652Z'
        }
    """
    output = {}
    if phase_codename == "dev":
        print("Evaluating for Dev Phase")
        output["result"] = [
            {
                "train_split": {
                    "Metric1": random.randint(0, 99),
                    "Metric2": random.randint(0, 99),
                    "Metric3": random.randint(0, 99),
                    "Total": random.randint(0, 99),
                }
            }
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][0]["train_split"]
        print("Completed evaluation for Dev Phase")
    elif phase_codename == "test":
        print("Evaluating for Test Phase")
        output["result"] = [
            {
                "train_split": {
                    "Metric1": random.randint(0, 99),
                    "Metric2": random.randint(0, 99),
                    "Metric3": random.randint(0, 99),
                    "Total": random.randint(0, 99),
                }
            },
            {
                "test_split": {
                    "Metric1": random.randint(0, 99),
                    "Metric2": random.randint(0, 99),
                    "Metric3": random.randint(0, 99),
                    "Total": random.randint(0, 99),
                }
            },
        ]
        # To display the results in the result file
        output["submission_result"] = output["result"][0]
        print("Completed evaluation for Test Phase")
    return output
# def evaluate(test_annotation_file, user_submission_file, phase_codename, **kwargs):
#     print("Starting Evaluation.....")
#     """
#     Evaluates the submission for a particular challenge phase and returns score
#     Arguments:

#         `test_annotations_file`: Path to test_annotation_file on the server
#         `user_submission_file`: Path to file submitted by the user
#         `phase_codename`: Phase to which submission is made

#         `**kwargs`: keyword arguments that contains additional submission
#         metadata that challenge hosts can use to send slack notification.
#         You can access the submission metadata
#         with kwargs['submission_metadata']

#         Example: A sample submission metadata can be accessed like this:
#         >>> print(kwargs['submission_metadata'])
#         {
#             'status': u'running',
#             'when_made_public': None,
#             'participant_team': 5,
#             'input_file': 'https://abc.xyz/path/to/submission/file.json',
#             'execution_time': u'123',
#             'publication_url': u'ABC',
#             'challenge_phase': 1,
#             'created_by': u'ABC',
#             'stdout_file': 'https://abc.xyz/path/to/stdout/file.json',
#             'method_name': u'Test',
#             'stderr_file': 'https://abc.xyz/path/to/stderr/file.json',
#             'participant_team_name': u'Test Team',
#             'project_url': u'http://foo.bar',
#             'method_description': u'ABC',
#             'is_public': False,
#             'submission_result_file': 'https://abc.xyz/path/result/file.json',
#             'id': 123,
#             'submitted_at': u'2017-03-20T19:22:03.880652Z'
#         }
#     """
#     output = {}
#     if phase_codename == "VG-RS":
#         print("Evaluating for VG-RS Phase")
#         # 读取JSON文件
#         # with open(test_annotation_file, 'r') as f:
#         #     user_data = json.load(f)
#         # with open(user_submission_file, 'r') as f:
#         #     test_data = json.load(f)
#         # # 构建用户提交数据的查找字典
#         # user_dict = {(item['image_path'], item['question']): item for item in user_data}
#         # # 存储结果
#         # accum_acc=0
#         # results = []
#         # # 遍历测试数据
#         # for item in test_data:
#         #     key = (item['image_path'], item['question'])
#         #     if key in user_dict:
#         #         # 获取两个result并计算IOU
#         #         box1 = item['result']
#         #         box2 = user_dict[key]['result']
#         #         iou = compute_iou(box1, box2)
#         #         results.append(iou)
#         #         if iou >= 0.5
#         #             accum_acc += 1
#         #     # else:
#         #     #     output["result"] = [{"train_split": {"ACC": NAN}}]
#         #     #     output["submission_result"] = output["result"][0]
#         #     #     return output
#         # # accum_acc = accum_acc / len(test_data)
#         # output["result"] = [{"train_split": {"ACC": accum_acc}}]
#         output["result"] = [
#         {
#             "train_split": {
#                 # "Metric1": random.randint(0, 99),
#                 # "Metric2": random.randint(0, 99),
#                 # "Metric3": random.randint(0, 99),
#                 "ACC": int(999998888),
#             }
#         },
#         # To display the results in the result file
#         output["submission_result"] = output["result"][0]
#         print("Completed evaluation for Dev Phase")
#     elif phase_codename == "VQA-SA":
#         print("Evaluating for VQA-SA Phase")
#         client = ZhipuAI(api_key=API_KEY)
#         response = client.chat.completions.create(
#             model="glm-4-flash",
#             messages=[
#                 {"role": "system", "content": "你是一个智能判断助手，你的任务是根据问题和给出的正确答案，分析模型的预测答案是是否正确回答了问题。如果正确，请回答1；如果错误，请回答0；注意，只能输出0或者1，不允许有任何其他内容输出。正确的预测必须完全符合标准答案的语义，否则被认为错误"},
#                 {"role": "user", "content": "问题是飞机在天上飞？;模型的预测答案是：是的}；正确答案是：是"}
#             ],
#             temperature=0.0,
#         )
#         is_true = response.choices[0].message.content
#         output["result"] = [
#             {
#                 "train_split": {
#                     # "Metric1": random.randint(0, 99),
#                     # "Metric2": random.randint(0, 99),
#                     # "Metric3": random.randint(0, 99),
#                     "ACC": int(9999000) + int(is_true),
#                 }
#             }
#         ]
#             # {
#             #     "test_split": {
#             #         # "Metric1": random.randint(0, 99),
#             #         # "Metric2": random.randint(0, 99),
#             #         # "Metric3": random.randint(0, 99),
#             #         "ACC": int(1009999),
#             #     }
#             # },
#         ]
#         # To display the results in the result file
#         output["submission_result"] = output["result"][0]
#         print("Completed evaluation for VQA-SA Phase")
#     elif phase_codename == "VR-Ads":
#         print("Evaluating for VR-Ads Phase")
#         output["result"] = [
#             {
#                 "train_split": {
#                     # "Metric1": random.randint(0, 99),
#                     # "Metric2": random.randint(0, 99),
#                     # "Metric3": random.randint(0, 99),
#                     "ACC": int(999999999),
#                 }
#             },
#             # {
#             #     "test_split": {
#             #         # "Metric1": random.randint(0, 99),
#             #         # "Metric2": random.randint(0, 99),
#             #         # "Metric3": random.randint(0, 99),
#             #         "ACC": int(1009999),
#             #     }
#             # },
#         ]
#         # To display the results in the result file
#         output["submission_result"] = output["result"][0]
#         print("Completed evaluation for VR-Ads Phase")
#     return output
