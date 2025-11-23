import json
import random
import datetime
import os

# 获取今天的日期
today = datetime.date.today().strftime("%Y-%m-%d")

# 模拟：各个模型的基础分（为了让数据看起来真实，我们设定一个基础分，然后随机波动）
base_scores = {
    "gpt-5-pro": {"logic": 9.5, "coding": 9.5, "writing": 9.3},
    "o1-preview": {"logic": 9.8, "coding": 9.1, "writing": 7.8},
    "gpt-4o": {"logic": 9.0, "coding": 8.8, "writing": 8.5},
    "claude-3-5-sonnet": {"logic": 8.8, "coding": 9.7, "writing": 9.5},
    "gemini-1-5-pro": {"logic": 8.4, "coding": 8.1, "writing": 8.0},
    "deepseek-v3": {"logic": 8.6, "coding": 8.9, "writing": 8.1}
}

# 模拟：生成模型列表数据
models_data = []
ranking = 1

for model_id, scores in base_scores.items():
    # 随机波动：让分数每天在 -0.2 到 +0.2 之间浮动
    fluctuation = random.uniform(-0.2, 0.2)
    
    # 模拟 DeepSeek 的 API 状态波动
    status = "stable"
    if model_id == "deepseek-v3" and random.random() > 0.7:
        status = "warning"
    
    models_data.append({
        "id": model_id,
        "name": model_id.replace("-", " ").title().replace("Gpt", "GPT"),
        "provider": "OpenAI" if "gpt" in model_id or "o1" in model_id else ("Anthropic" if "claude" in model_id else ("Google" if "gemini" in model_id else "DeepSeek")),
        "type": "Reasoning" if "o1" in model_id else "General",
        "globalRank": ranking,
        "rankChange": random.randint(-2, 2), # 模拟排名升降
        "isNew": True if model_id == "gpt-5-pro" else False,
        "scores": {
            "logic": round(scores["logic"] + fluctuation, 1),
            "coding": round(scores["coding"] + fluctuation, 1),
            "writing": round(scores["writing"] + fluctuation, 1),
            "context": round(random.uniform(8.0, 9.9), 1),
            "instruction": round(random.uniform(8.5, 9.8), 1),
            "safety": round(random.uniform(7.5, 9.5), 1)
        },
        "status": status,
        "tags": ["热门", "推荐"] if ranking <= 2 else ["稳定"],
        "price": "$$$" if ranking <= 3 else "$"
    })
    ranking += 1

# 组合最终数据
daily_report = {
    "date": today,
    "updateTime": datetime.datetime.utcnow().strftime("%H:%M UTC"),
    "totalMonitored": 52,
    "newEntries": random.randint(0, 3),
    "dropped": random.randint(0, 2),
    "models": models_data
}

# 将数据写入到 data.json 文件中
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(daily_report, f, indent=2, ensure_ascii=False)

print(f"✅ 成功生成 {today} 的 AI 评测报告！")
