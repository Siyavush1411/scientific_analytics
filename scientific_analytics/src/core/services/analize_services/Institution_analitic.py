import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict

plt.style.use('ggplot')

class DataVisualizer:
    @staticmethod
    def _prepare_figure(title: str, figsize=(10, 6)):
        fig, ax = plt.subplots(figsize=figsize)
        ax.set_title(title, pad=20, fontsize=14, fontweight='bold')
        return fig, ax

    @staticmethod
    def plot_institution_type_stats(data: List[Dict], figsize=(12, 8)):
        """Визуализация статистики по типам учреждений"""
        if not data:
            return

        types = [item['institution_type'] for item in data]
        metrics = ['count', 'avg_rating', 'total_works']
        labels = ['Количество', 'Средний рейтинг', 'Всего работ']

        fig, axs = plt.subplots(3, 1, figsize=figsize)
        
        for i, metric in enumerate(metrics):
            values = [item[metric] or 0 for item in data]
            axs[i].bar(types, values, color=plt.cm.Paired(i/3))
            axs[i].set_ylabel(labels[i])
            axs[i].tick_params(axis='x', rotation=45)
            
        plt.tight_layout()
        return fig

    @staticmethod
    def plot_top_institutions(data: List[Dict], figsize=(10, 6)):
        """Топ учреждений по количеству работ"""
        institutions = [item['name'] for item in data][::-1]
        works = [item['total_works'] for item in data][::-1]

        fig, ax = DataVisualizer._prepare_figure(
            "Топ учреждений по количеству научных работ",
            figsize
        )
        
        y_pos = np.arange(len(institutions))
        ax.barh(y_pos, works, color='teal')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(institutions)
        ax.set_xlabel('Количество работ')
        plt.tight_layout()
        return fig

    @staticmethod
    def plot_category_stats(data: List[Dict], figsize=(12, 6)):
        """Визуализация статистики по категориям работт"""
        categories = [item['category__name'] for item in data]
        
        fig, axs = plt.subplots(1, 3, figsize=figsize)
        metrics = {
            'count': ('Количество работ', 'skyblue'),
            'avg_rating': ('Средний рейтинг', 'salmon'),
            'avg_uniqueness': ('Уникальность', 'lightgreen')
        }

        for i, (metric, (title, color)) in enumerate(metrics.items()):
            values = [item[metric] or 0 for item in data]
            axs[i].barh(categories[::-1], values[::-1], color=color)
            axs[i].set_title(title)
            
        plt.tight_layout()
        return fig

    @staticmethod
    def plot_user_status_distribution(data: List[Dict], figsize=(8, 8)):
        """Распределение пользователей по статусам"""
        labels = [f"{item['status__name']} ({item['count']})" for item in data]
        sizes = [item['count'] for item in data]

        fig, ax = DataVisualizer._prepare_figure(
            "Распределение пользователей по статусам",
            figsize
        )
        
        ax.pie(
            sizes, 
            labels=labels, 
            autopct='%1.1f%%',
            startangle=90,
            colors=plt.cm.Pastel1.colors
        )
        ax.axis('equal')
        return fig

    @staticmethod
    def plot_top_users(data: List[Dict], figsize=(10, 6)):
        """Топ пользователей по рейтингу"""
        users = [f"{item['username']}\n({item['institution__name']})" for item in data]
        ratings = [item['rating'] for item in data]

        fig, ax = DataVisualizer._prepare_figure(
            "Топ пользователей по рейтингу",
            figsize
        )
        
        y_pos = np.arange(len(users))
        bars = ax.barh(y_pos, ratings, color='purple')
        ax.bar_label(bars, padding=3, labels=[f"{r} pts" for r in ratings])
        ax.set_yticks(y_pos)
        ax.set_yticklabels(users)
        ax.set_xlabel('Рейтинг')
        plt.tight_layout()
        return fig

    @staticmethod
    def plot_work_distribution(data: List[Dict], figsize=(10, 6)):
        """Распределение количества работ среди пользователей"""
        works = [item['works_count'] for item in data]
        users = [item['users_count'] for item in data]

        fig, ax = DataVisualizer._prepare_figure(
            "Распределение количества работ среди пользователей",
            figsize
        )
        
        ax.bar(works, users, color='orange')
        ax.set_xlabel('Количество работ')
        ax.set_ylabel('Количество пользователей')
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        return fig