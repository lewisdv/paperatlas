#!/usr/bin/env python3

import argparse
import html
import json
import math
import os
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from jinja2 import Template
from workspace import PROJECT_ROOT, list_collection_workspaces, read_collection_metadata, resolve_workspace


ROOT = PROJECT_ROOT
WIKI_DIR = ROOT / "wiki"
OUTPUT_DIR = ROOT / "wiki_html"
ASSETS_DIR = OUTPUT_DIR / "assets"
STYLE_PATH = ASSETS_DIR / "style.css"
SOURCE_ASSETS_DIR = PROJECT_ROOT / "assets"
LOGO_FILENAME = "paper_atlas_logo.svg"
LOGO_SOURCE_PATH = SOURCE_ASSETS_DIR / LOGO_FILENAME
WORKSPACE_TITLE = "Research Collection"
WORKSPACE_DESCRIPTION = "Static HTML view of the Markdown research wiki."
SITE_BRAND = "paper_atlas"
LOCAL_VIEWER_HOST = "127.0.0.1"
LOCAL_VIEWER_PORT = 8765
LOCAL_VIEWER_BASE = f"http://{LOCAL_VIEWER_HOST}:{LOCAL_VIEWER_PORT}"
GRAPH_VIEWBOX_WIDTH = 1080
GRAPH_VIEWBOX_HEIGHT = 720
PUBLIC_SITE_MODE = False
PUBLIC_SITE_INCLUDE_PDFS = False


def configure_workspace(root: Path, title: str, description: str) -> None:
    global ROOT, WIKI_DIR, OUTPUT_DIR, ASSETS_DIR, STYLE_PATH
    global WORKSPACE_TITLE, WORKSPACE_DESCRIPTION

    ROOT = root
    WIKI_DIR = ROOT / "wiki"
    OUTPUT_DIR = ROOT / "wiki_html"
    ASSETS_DIR = OUTPUT_DIR / "assets"
    STYLE_PATH = ASSETS_DIR / "style.css"
    WORKSPACE_TITLE = title
    WORKSPACE_DESCRIPTION = description


def configure_render_mode(*, public_site: bool, include_pdfs: bool) -> None:
    global PUBLIC_SITE_MODE, PUBLIC_SITE_INCLUDE_PDFS
    PUBLIC_SITE_MODE = public_site
    PUBLIC_SITE_INCLUDE_PDFS = include_pdfs


def http_href_for_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        relative = resolved.relative_to(PROJECT_ROOT).as_posix()
    except ValueError:
        return resolved.as_uri()
    return f"{LOCAL_VIEWER_BASE}/{relative}"

SECTION_LABELS = {
    "": "Core",
    "sources": "Sources",
    "concepts": "Concepts",
    "queries": "Queries",
    "syntheses": "Syntheses",
}
SECTION_ORDER = ["", "sources", "concepts", "queries", "syntheses"]
SECTION_TAGS = {
    "": "Core",
    "sources": "Paper",
    "concepts": "Concept",
    "queries": "Query",
    "syntheses": "Synthesis",
}
SECTION_COLORS = {
    "": "#946448",
    "sources": "#8e3c27",
    "concepts": "#275d5d",
    "queries": "#755f24",
    "syntheses": "#4f3a77",
}

UI_TRANSLATIONS = {
    "en": {
        "language": "Language",
        "english": "English",
        "korean": "한국어",
        "workspace_description": "Static HTML view of the Markdown research wiki.",
        "wiki_suffix": " Wiki",
        "atlas_suffix": " Research Atlas",
        "home": "Home",
        "open_dashboard": "Open Interactive Dashboard",
        "open_local_viewer": "Open Local Viewer",
        "generated_label": "Generated",
        "metadata": "Metadata",
        "search": "Search",
        "search_placeholder": "Search titles, summaries, tags, and page text",
        "search_help": "Works across all pages, then narrows paper cards, database view, list view, and graph view together.",
        "views": "Views",
        "view_papers": "Paper Cards",
        "view_database": "Database",
        "view_pages": "All Pages",
        "view_graph": "Graph View",
        "tag_filter": "Tag Filter",
        "clear": "Clear",
        "quick_links": "Quick Links",
        "sections": "Sections",
        "interactive_dashboard": "Interactive Dashboard",
        "hero_copy": "One page for paper cards, full-page browsing, search, tag filters, and a graph of how the Markdown wiki links together.",
        "pages": "Pages",
        "papers": "Papers",
        "concepts": "Concepts",
        "relations": "Relations",
        "no_papers_match": "No papers match the current search and tags.",
        "no_pages_match": "No pages match the current search and tags.",
        "graph_toolbar": "Only paper nodes are shown here. Edges represent direct paper links or shared themes such as organ, method, maturation strategy, or assay focus.",
        "graph_detail": "Graph Detail",
        "select_node": "Select a node",
        "graph_detail_help": "The graph groups papers by their main theme and connects papers that share substantive topics or directly reference one another. Use the controls to tune node size, edge width, label density, repulsion, link distance, and label visibility.",
        "graph_controls": "Graph Controls",
        "graph_node_size": "Node Size",
        "graph_edge_width": "Edge Width",
        "graph_label_density": "Label Density",
        "graph_repulsion": "Repulsion",
        "graph_link_distance": "Link Distance",
        "graph_show_labels": "Show Labels",
        "graph_toggle_on": "On",
        "graph_toggle_off": "Off",
        "graph_reset": "Reset Graph",
        "database_controls": "Database Controls",
        "database_sort": "Sort",
        "database_group": "Group",
        "database_export": "Export CSV",
        "database_density": "Density",
        "database_density_comfortable": "Comfortable",
        "database_density_compact": "Compact",
        "database_sort_title": "Title",
        "database_sort_year": "Year",
        "database_sort_section": "Section",
        "database_sort_status": "Status",
        "database_sort_relations": "Relations",
        "database_sort_recent": "Recent",
        "database_group_none": "No Group",
        "database_group_section": "Section",
        "database_group_status": "Status",
        "database_group_year": "Year",
        "database_group_graph": "Theme",
        "database_column_title": "Title",
        "database_column_section": "Section",
        "database_column_year": "Year",
        "database_column_status": "Status",
        "database_column_theme": "Theme",
        "database_column_relations": "Relations",
        "database_column_tags": "Tags",
        "database_column_actions": "Actions",
        "database_empty": "No rows match the current search and filters.",
        "database_summary_rows": "Rows",
        "database_summary_papers": "Papers",
        "database_summary_years": "Year Range",
        "database_summary_groups": "Groups",
        "database_unspecified": "Unspecified",
        "database_group_untitled": "Other",
        "database_export_filename": "paper-collect-view",
        "match_detail": "Search and tag filters apply across cards, database view, list view, and the paper relationship graph.",
        "search_prefix": "Search",
        "open_page": "Open Page",
        "open": "Open",
        "open_pdf": "Open PDF",
        "open_article": "Journal Page",
        "no_relationship_tags": "No inferred relationship tags yet",
        "related_papers": "Related Papers",
        "no_related_papers": "No paper-to-paper relationships are visible for this paper under the current filters.",
        "no_papers_graph": "No papers match the current search and tags.",
        "direct_wiki_link": "Direct Wiki Link",
        "graph_theme_legend": "Theme Legend",
        "graph_metric_theme": "Theme",
        "graph_metric_relations": "Visible Relations",
        "graph_metric_year": "Year",
    },
    "ko": {
        "language": "언어",
        "english": "English",
        "korean": "한국어",
        "workspace_description": "Markdown 연구 위키를 정적 HTML로 보여줍니다.",
        "wiki_suffix": " 위키",
        "atlas_suffix": " 연구 아틀라스",
        "home": "홈",
        "open_dashboard": "인터랙티브 대시보드 열기",
        "open_local_viewer": "로컬 뷰어 열기",
        "generated_label": "생성 시각",
        "metadata": "메타데이터",
        "search": "검색",
        "search_placeholder": "제목, 요약, 태그, 페이지 본문 검색",
        "search_help": "모든 페이지를 대상으로 검색한 뒤, 논문 카드, 데이터베이스, 전체 목록, 그래프 뷰에 함께 적용됩니다.",
        "views": "보기",
        "view_papers": "논문 카드",
        "view_database": "데이터베이스",
        "view_pages": "전체 페이지",
        "view_graph": "그래프 뷰",
        "tag_filter": "태그 필터",
        "clear": "초기화",
        "quick_links": "바로가기",
        "sections": "섹션",
        "interactive_dashboard": "인터랙티브 대시보드",
        "hero_copy": "논문 카드, 전체 페이지 탐색, 검색, 태그 필터, 그리고 Markdown 위키의 연결 관계를 한 화면에서 볼 수 있습니다.",
        "pages": "페이지",
        "papers": "논문",
        "concepts": "개념",
        "relations": "관계",
        "no_papers_match": "현재 검색어와 태그에 맞는 논문이 없습니다.",
        "no_pages_match": "현재 검색어와 태그에 맞는 페이지가 없습니다.",
        "graph_toolbar": "여기에는 논문 노드만 표시됩니다. 선은 직접 논문 링크이거나 장기, 방법, 성숙화 전략, 분석 초점 같은 공통 주제를 뜻합니다.",
        "graph_detail": "그래프 상세",
        "select_node": "노드를 선택하세요",
        "graph_detail_help": "그래프는 논문을 주요 주제별로 묶고, 실질적인 공통점이나 직접 참조가 있는 논문끼리 연결합니다. 아래 컨트롤로 노드 크기, 엣지 두께, 라벨 밀도, 반발력, 링크 거리, 라벨 표시 여부를 조절할 수 있습니다.",
        "graph_controls": "그래프 조절",
        "graph_node_size": "노드 크기",
        "graph_edge_width": "엣지 두께",
        "graph_label_density": "라벨 밀도",
        "graph_repulsion": "반발력",
        "graph_link_distance": "링크 거리",
        "graph_show_labels": "라벨 표시",
        "graph_toggle_on": "켜짐",
        "graph_toggle_off": "꺼짐",
        "graph_reset": "그래프 초기화",
        "database_controls": "데이터베이스 조절",
        "database_sort": "정렬",
        "database_group": "그룹",
        "database_export": "CSV 내보내기",
        "database_density": "밀도",
        "database_density_comfortable": "보통",
        "database_density_compact": "촘촘하게",
        "database_sort_title": "제목",
        "database_sort_year": "연도",
        "database_sort_section": "섹션",
        "database_sort_status": "상태",
        "database_sort_relations": "관계 수",
        "database_sort_recent": "최근순",
        "database_group_none": "그룹 없음",
        "database_group_section": "섹션",
        "database_group_status": "상태",
        "database_group_year": "연도",
        "database_group_graph": "주제",
        "database_column_title": "제목",
        "database_column_section": "섹션",
        "database_column_year": "연도",
        "database_column_status": "상태",
        "database_column_theme": "주제",
        "database_column_relations": "관계 수",
        "database_column_tags": "태그",
        "database_column_actions": "동작",
        "database_empty": "현재 검색어와 필터에 맞는 행이 없습니다.",
        "database_summary_rows": "행",
        "database_summary_papers": "논문",
        "database_summary_years": "연도 범위",
        "database_summary_groups": "그룹",
        "database_unspecified": "미지정",
        "database_group_untitled": "기타",
        "database_export_filename": "paper-collect-view",
        "match_detail": "검색과 태그 필터는 카드, 데이터베이스, 목록, 논문 관계 그래프에 함께 적용됩니다.",
        "search_prefix": "검색",
        "open_page": "페이지 열기",
        "open": "열기",
        "open_pdf": "PDF 열기",
        "open_article": "저널 페이지",
        "no_relationship_tags": "아직 추론된 관계 태그가 없습니다",
        "related_papers": "연관 논문",
        "no_related_papers": "현재 필터 기준으로 이 논문과 연결된 다른 논문이 보이지 않습니다.",
        "no_papers_graph": "현재 검색어와 태그에 맞는 논문이 없습니다.",
        "direct_wiki_link": "직접 위키 링크",
        "graph_theme_legend": "주제 범례",
        "graph_metric_theme": "주제",
        "graph_metric_relations": "보이는 관계",
        "graph_metric_year": "연도",
    },
}

LABEL_TRANSLATIONS = {
    "ko": {
        "Overview": "개요",
        "Index Note": "인덱스 노트",
        "Log": "로그",
        "Latest Synthesis": "최신 종합 정리",
        "Core": "코어",
        "Sources": "소스",
        "Concepts": "개념",
        "Queries": "질의",
        "Syntheses": "종합 정리",
        "Paper": "논문",
        "Concept": "개념",
        "Query": "질의",
        "Synthesis": "종합 정리",
        "Queued": "대기 중",
        "Open": "열림",
        "Ingested": "인제스트 완료",
        "Brain": "뇌",
        "Colon / Intestine": "대장 / 장",
        "Kidney": "신장",
        "Heart": "심장",
        "Liver": "간",
        "Pancreas / Biliary": "췌장 / 담도",
        "Lung": "폐",
        "Tumor / Cancer": "종양 / 암",
        "Breast": "유방",
        "Prostate": "전립선",
        "Rare Disease": "희귀질환",
        "Clinical": "임상",
        "Population": "집단",
        "Single Cell": "단일세포",
        "Structural Variation": "구조변이",
        "Benchmark": "벤치마크",
        "Methylation": "메틸레이션",
        "HiFi": "HiFi",
        "ONT": "ONT",
        "Biobank": "바이오뱅크",
        "Assembloid": "어셈블로이드",
        "Neuronal Migration": "신경세포 이동",
        "ALI Slice Culture": "ALI 슬라이스 배양",
        "Long-Term Maturation": "장기 성숙화",
        "Gene Editing": "유전자 편집",
        "Transplantation": "이식",
        "Coculture": "공배양",
        "Other Papers": "기타 논문",
        "Direct Wiki Link": "직접 위키 링크",
        "raw source": "원본 파일",
        "kind": "유형",
        "status": "상태",
        "added": "추가일",
        "created": "생성일",
        "article url": "논문 URL",
        "pdf url": "PDF URL",
        "title": "제목",
    }
}

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
ORDERED_LIST_RE = re.compile(r"^\d+\.\s+(.*)$")
UNORDERED_LIST_RE = re.compile(r"^-\s+(.*)$")


PAGE_TEMPLATE = Template(
    """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ page.title }} | {{ workspace_title }} wiki | {{ site_brand }}</title>
    <link rel="stylesheet" href="{{ stylesheet_href }}">
  </head>
  <body>
    <div class="shell">
      <aside class="sidebar">
        <div class="brand">
          <div class="brand-topbar">
            <a
              class="home-logo-link"
              href="{{ home_href }}"
              data-file-href="{{ home_file_href }}"
              data-http-href="{{ home_http_href }}"
              data-i18n-title="home"
            >
              <img class="home-logo-mark" src="{{ logo_href }}" alt="">
              <span class="home-logo-text">{{ site_brand }}</span>
            </a>
            <p class="eyebrow">{{ site_brand }}</p>
          </div>
          <a class="brand-link" href="{{ dashboard_href }}" data-file-href="{{ dashboard_file_href }}" data-http-href="{{ dashboard_http_href }}">
            <h1><span>{{ workspace_title }}</span><span data-i18n-key="wiki_suffix"> Wiki</span></h1>
          </a>
          <p class="subtle" data-i18n-key="workspace_description">{{ workspace_description }}</p>
          <div class="language-toggle" role="group" aria-label="Language toggle">
            <span class="control-label" data-i18n-key="language">Language</span>
            <div class="language-buttons">
              <button class="lang-button active" type="button" data-lang="en" data-i18n-key="english">English</button>
              <button class="lang-button" type="button" data-lang="ko" data-i18n-key="korean">한국어</button>
            </div>
          </div>
          <div class="brand-actions">
            <a class="dashboard-link" href="{{ dashboard_href }}" data-file-href="{{ dashboard_file_href }}" data-http-href="{{ dashboard_http_href }}" data-i18n-key="open_dashboard">Open Interactive Dashboard</a>
            {% if show_local_viewer_link %}
            <a class="dashboard-link secondary-link" href="{{ dashboard_http_href }}" data-i18n-key="open_local_viewer">Open Local Viewer</a>
            {% endif %}
          </div>
        </div>
        {% for section in navigation %}
        <section class="nav-group">
          <h2 data-i18n-label="{{ section.label }}">{{ section.label }}</h2>
          <ul>
            {% for item in section.entries %}
            <li class="{% if item.current %}current{% endif %}">
              <a href="{{ item.href }}" data-file-href="{{ item.file_href }}" data-http-href="{{ item.http_href }}">{{ item.title }}</a>
            </li>
            {% endfor %}
          </ul>
        </section>
        {% endfor %}
      </aside>
      <main class="content">
        <header class="page-header">
          <div>
            <p class="eyebrow" data-i18n-label="{{ page.section_label }}">{{ page.section_label }}</p>
            <h1>{{ page.title }}</h1>
          </div>
          <div class="meta-chip">
            <span data-i18n-key="generated_label">Generated</span> {{ generated_at }}
          </div>
        </header>

        {% if page.meta_items %}
        <section class="meta-panel">
          <h2 data-i18n-key="metadata">Metadata</h2>
          <dl>
            {% for key, value in page.meta_items %}
            <div>
              <dt data-i18n-label="{{ key }}">{{ key }}</dt>
              <dd>{{ value }}</dd>
            </div>
            {% endfor %}
          </dl>
        </section>
        {% endif %}

        <article class="page-body">
          {{ page.content | safe }}
        </article>
      </main>
    </div>
    <script id="page-i18n-data" type="application/json">{{ i18n_data_json | safe }}</script>
    <script>
      (() => {
        const i18nData = JSON.parse(document.getElementById("page-i18n-data").textContent);
        const state = {
          language: localStorage.getItem("paper_atlas_lang") || "en",
        };
        const langButtons = Array.from(document.querySelectorAll(".lang-button"));

        function t(key) {
          return (i18nData.ui[state.language] || {})[key]
            || (i18nData.ui.en || {})[key]
            || key;
        }

        function translateLabel(label) {
          return (i18nData.labels[state.language] || {})[label]
            || (i18nData.labels.en || {})[label]
            || label;
        }

        let localViewerProbe = null;

        function isFileModeNavigation() {
          return window.location.protocol === "file:" || !/^https?:$/.test(window.location.protocol);
        }

        function getLocalViewerOrigin(httpHref) {
          try {
            return new URL(httpHref).origin;
          } catch (_error) {
            return "";
          }
        }

        function canReachLocalViewer(httpHref) {
          const origin = getLocalViewerOrigin(httpHref);
          if (!origin) {
            return Promise.resolve(false);
          }
          if (localViewerProbe && localViewerProbe.origin === origin) {
            return localViewerProbe.promise;
          }
          localViewerProbe = {
            origin,
            promise: new Promise((resolve) => {
              const controller = typeof AbortController === "function" ? new AbortController() : null;
              const timeoutId = window.setTimeout(() => {
                if (controller) {
                  controller.abort();
                }
                resolve(false);
              }, 450);
              fetch(`${origin}/__paper_collect_ping__`, {
                method: "GET",
                cache: "no-store",
                mode: "no-cors",
                signal: controller ? controller.signal : undefined,
              })
                .then(() => {
                  window.clearTimeout(timeoutId);
                  resolve(true);
                })
                .catch(() => {
                  window.clearTimeout(timeoutId);
                  resolve(false);
                });
            }),
          };
          return localViewerProbe.promise;
        }

        async function preferredNavigationTarget(link) {
          const fileHref = link.getAttribute("data-file-href");
          const httpHref = link.getAttribute("data-http-href");
          const href = link.getAttribute("href");
          if (!isFileModeNavigation()) {
            return href || httpHref || fileHref || "#";
          }
          if (httpHref && await canReachLocalViewer(httpHref)) {
            return httpHref;
          }
          return fileHref || href || httpHref || "#";
        }

        document.addEventListener("click", async (event) => {
          const link = event.target.closest ? event.target.closest("a[data-file-href], a[data-http-href]") : null;
          if (!link || !isFileModeNavigation()) {
            return;
          }
          if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
            return;
          }
          event.preventDefault();
          const target = await preferredNavigationTarget(link);
          if (target) {
            window.location.assign(target);
          }
        });

        function applyLanguage() {
          document.documentElement.lang = state.language === "ko" ? "ko" : "en";
          document.querySelectorAll("[data-i18n-key]").forEach((element) => {
            element.textContent = t(element.dataset.i18nKey);
          });
          document.querySelectorAll("[data-i18n-title]").forEach((element) => {
            const label = t(element.dataset.i18nTitle);
            element.setAttribute("title", label);
            element.setAttribute("aria-label", label);
          });
          document.querySelectorAll("[data-i18n-label]").forEach((element) => {
            element.textContent = translateLabel(element.dataset.i18nLabel);
          });
          langButtons.forEach((button) => {
            button.classList.toggle("active", button.dataset.lang === state.language);
          });
        }

        langButtons.forEach((button) => {
          button.addEventListener("click", () => {
            state.language = button.dataset.lang;
            localStorage.setItem("paper_atlas_lang", state.language);
            applyLanguage();
          });
        });

        applyLanguage();
      })();
    </script>
  </body>
</html>
"""
)


DASHBOARD_TEMPLATE = Template(
    """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{{ workspace_title }} Dashboard | {{ site_brand }}</title>
    <link rel="stylesheet" href="assets/style.css">
  </head>
  <body>
    <div class="shell dashboard-shell">
      <input class="view-state-toggle" type="radio" name="dashboard-view-state" id="view-tab-papers" data-view="papers" checked>
      <input class="view-state-toggle" type="radio" name="dashboard-view-state" id="view-tab-database" data-view="database">
      <input class="view-state-toggle" type="radio" name="dashboard-view-state" id="view-tab-pages" data-view="pages">
      <input class="view-state-toggle" type="radio" name="dashboard-view-state" id="view-tab-graph" data-view="graph">
      <aside class="sidebar dashboard-sidebar">
        <div class="brand">
          <div class="brand-topbar">
            <a
              class="home-logo-link"
              href="{{ home_href }}"
              data-file-href="{{ home_file_href }}"
              data-http-href="{{ home_http_href }}"
              data-i18n-title="home"
            >
              <img class="home-logo-mark" src="{{ logo_href }}" alt="">
              <span class="home-logo-text">{{ site_brand }}</span>
            </a>
            <p class="eyebrow">{{ site_brand }}</p>
          </div>
          <h1><span>{{ workspace_title }}</span><span data-i18n-key="wiki_suffix"> Wiki</span></h1>
          <p class="subtle" data-i18n-key="workspace_description">{{ workspace_description }}</p>
          <div class="language-toggle" role="group" aria-label="Language toggle">
            <span class="control-label" data-i18n-key="language">Language</span>
            <div class="language-buttons">
              <button class="lang-button active" type="button" data-lang="en" data-i18n-key="english">English</button>
              <button class="lang-button" type="button" data-lang="ko" data-i18n-key="korean">한국어</button>
            </div>
          </div>
          <div class="brand-actions">
            {% if show_local_viewer_link %}
            <a class="dashboard-link secondary-link" href="{{ dashboard_http_href }}" data-i18n-key="open_local_viewer">Open Local Viewer</a>
            {% endif %}
          </div>
        </div>

        <section class="side-block">
          <label class="control-label" for="search-input" data-i18n-key="search">Search</label>
          <input id="search-input" class="search-input" type="search" placeholder="Search titles, summaries, tags, and page text" data-i18n-placeholder="search_placeholder">
          <p class="subtle small-note" data-i18n-key="search_help">Works across all pages, then narrows papers, list view, and graph view together.</p>
        </section>

        <section class="side-block">
          <p class="control-label" data-i18n-key="views">Views</p>
          <div class="view-switch" id="view-switch">
            <label class="view-button" data-view="papers" for="view-tab-papers" role="button" tabindex="0" data-i18n-key="view_papers">Paper Cards</label>
            <label class="view-button" data-view="database" for="view-tab-database" role="button" tabindex="0" data-i18n-key="view_database">Database</label>
            <label class="view-button" data-view="pages" for="view-tab-pages" role="button" tabindex="0" data-i18n-key="view_pages">All Pages</label>
            <label class="view-button" data-view="graph" for="view-tab-graph" role="button" tabindex="0" data-i18n-key="view_graph">Graph View</label>
          </div>
        </section>

        <section class="side-block">
          <div class="side-header">
            <p class="control-label" data-i18n-key="tag_filter">Tag Filter</p>
            <button id="clear-filters" class="ghost-button" type="button" data-i18n-key="clear">Clear</button>
          </div>
          <div id="tag-chips" class="chip-list"></div>
        </section>

        <section class="side-block">
          <p class="control-label" data-i18n-key="quick_links">Quick Links</p>
          <ul class="quick-links">
            {% for item in quick_links %}
            <li><a href="{{ item.href }}" data-file-href="{{ item.file_href }}" data-http-href="{{ item.http_href }}" data-i18n-label="{{ item.label }}">{{ item.label }}</a></li>
            {% endfor %}
          </ul>
        </section>

        <section class="side-block">
          <p class="control-label" data-i18n-key="sections">Sections</p>
          <div class="legend-list">
            {% for section in section_legend %}
            <div class="legend-row">
              <span class="legend-dot" style="background: {{ section.color }}"></span>
              <span data-i18n-label="{{ section.label }}">{{ section.label }}</span>
              <span class="legend-count">{{ section.count }}</span>
            </div>
            {% endfor %}
          </div>
        </section>
      </aside>

      <main class="content dashboard-content">
        <header class="dashboard-hero">
          <div>
            <p class="eyebrow" data-i18n-key="interactive_dashboard">Interactive Dashboard</p>
            <h1><span>{{ workspace_title }}</span><span data-i18n-key="atlas_suffix"> Research Atlas</span></h1>
            <p class="hero-copy" data-i18n-key="hero_copy">
              One page for paper cards, full-page browsing, search, tag filters, and a graph of how the Markdown wiki links together.
            </p>
          </div>
          <div class="hero-stats">
            <article class="stat-card">
              <span class="stat-label" data-i18n-key="pages">Pages</span>
              <strong>{{ counts.pages }}</strong>
            </article>
            <article class="stat-card">
              <span class="stat-label" data-i18n-key="papers">Papers</span>
              <strong>{{ counts.papers }}</strong>
            </article>
            <article class="stat-card">
              <span class="stat-label" data-i18n-key="concepts">Concepts</span>
              <strong>{{ counts.concepts }}</strong>
            </article>
            <article class="stat-card">
              <span class="stat-label" data-i18n-key="relations">Relations</span>
              <strong>{{ counts.edges }}</strong>
            </article>
          </div>
        </header>

        <section class="status-bar">
          <div class="status-copy">
            <strong id="match-summary"></strong>
            <span id="match-detail" class="subtle"></span>
          </div>
          <div id="active-filters" class="active-filters"></div>
        </section>

        <section id="papers-view" class="dashboard-view active">
          <div id="paper-grid" class="paper-grid">{{ initial_paper_grid_html | safe }}</div>
          <p id="papers-empty" class="empty-state hidden" data-i18n-key="no_papers_match">No papers match the current search and tags.</p>
        </section>

        <section id="database-view" class="dashboard-view hidden">
          <div class="database-toolbar">
            <div class="database-toolbar-head">
              <p class="control-label" data-i18n-key="database_controls">Database Controls</p>
              <button id="database-export" class="ghost-button" type="button" data-i18n-key="database_export">Export CSV</button>
            </div>
            <div class="database-controls">
              <label class="database-control">
                <span data-i18n-key="database_sort">Sort</span>
                <div class="database-inline-controls">
                  <select id="database-sort">
                    <option value="recent" data-i18n-key="database_sort_recent">Recent</option>
                    <option value="year" data-i18n-key="database_sort_year">Year</option>
                    <option value="title" data-i18n-key="database_sort_title">Title</option>
                    <option value="section" data-i18n-key="database_sort_section">Section</option>
                    <option value="status" data-i18n-key="database_sort_status">Status</option>
                    <option value="relations" data-i18n-key="database_sort_relations">Relations</option>
                  </select>
                  <button id="database-sort-direction" class="ghost-button database-icon-button" type="button">↓</button>
                </div>
              </label>
              <label class="database-control">
                <span data-i18n-key="database_group">Group</span>
                <select id="database-group">
                  <option value="none" data-i18n-key="database_group_none">No Group</option>
                  <option value="section" data-i18n-key="database_group_section">Section</option>
                  <option value="status" data-i18n-key="database_group_status">Status</option>
                  <option value="year" data-i18n-key="database_group_year">Year</option>
                  <option value="graph" data-i18n-key="database_group_graph">Theme</option>
                </select>
              </label>
              <label class="database-control">
                <span data-i18n-key="database_density">Density</span>
                <select id="database-density">
                  <option value="comfortable" data-i18n-key="database_density_comfortable">Comfortable</option>
                  <option value="compact" data-i18n-key="database_density_compact">Compact</option>
                </select>
              </label>
            </div>
            <div id="database-summary" class="database-summary">{{ initial_database_summary_html | safe }}</div>
          </div>
          <div id="database-groups" class="database-groups">{{ initial_database_groups_html | safe }}</div>
          <p id="database-empty" class="empty-state hidden" data-i18n-key="database_empty">No rows match the current search and filters.</p>
        </section>

        <section id="pages-view" class="dashboard-view hidden">
          <div id="page-list" class="page-list">{{ initial_page_list_html | safe }}</div>
          <p id="pages-empty" class="empty-state hidden" data-i18n-key="no_pages_match">No pages match the current search and tags.</p>
        </section>

        <section id="graph-view" class="dashboard-view hidden">
          <div class="graph-toolbar">
            <div class="graph-toolbar-copy subtle" data-i18n-key="graph_toolbar">{{ graph_toolbar_default }}</div>
            <div class="graph-controls-panel">
              <p class="control-label graph-controls-heading" data-i18n-key="graph_controls">Graph Controls</p>
              <div class="graph-controls">
                <label class="graph-control" for="graph-node-scale">
                  <span class="graph-control-row">
                    <span data-i18n-key="graph_node_size">Node Size</span>
                    <span id="graph-node-scale-value" class="graph-control-value">72%</span>
                  </span>
                  <input id="graph-node-scale" class="graph-range" type="range" min="55" max="140" step="1" value="72">
                </label>
                <label class="graph-control" for="graph-edge-scale">
                  <span class="graph-control-row">
                    <span data-i18n-key="graph_edge_width">Edge Width</span>
                    <span id="graph-edge-scale-value" class="graph-control-value">95%</span>
                  </span>
                  <input id="graph-edge-scale" class="graph-range" type="range" min="55" max="170" step="1" value="95">
                </label>
                <label class="graph-control" for="graph-label-density">
                  <span class="graph-control-row">
                    <span data-i18n-key="graph_label_density">Label Density</span>
                    <span id="graph-label-density-value" class="graph-control-value">70%</span>
                  </span>
                  <input id="graph-label-density" class="graph-range" type="range" min="35" max="150" step="1" value="70">
                </label>
                <label class="graph-control" for="graph-repulsion-scale">
                  <span class="graph-control-row">
                    <span data-i18n-key="graph_repulsion">Repulsion</span>
                    <span id="graph-repulsion-scale-value" class="graph-control-value">100%</span>
                  </span>
                  <input id="graph-repulsion-scale" class="graph-range" type="range" min="45" max="180" step="1" value="100">
                </label>
                <label class="graph-control" for="graph-link-distance-scale">
                  <span class="graph-control-row">
                    <span data-i18n-key="graph_link_distance">Link Distance</span>
                    <span id="graph-link-distance-scale-value" class="graph-control-value">100%</span>
                  </span>
                  <input id="graph-link-distance-scale" class="graph-range" type="range" min="60" max="165" step="1" value="100">
                </label>
                <label class="graph-control graph-toggle" for="graph-show-labels">
                  <span class="graph-control-row">
                    <span data-i18n-key="graph_show_labels">Show Labels</span>
                    <span id="graph-show-labels-value" class="graph-control-value">On</span>
                  </span>
                  <input id="graph-show-labels" class="graph-toggle-input" type="checkbox" checked>
                </label>
                <div class="graph-control graph-control-action">
                  <button id="graph-reset-controls" class="ghost-button" type="button" data-i18n-key="graph_reset">Reset Graph</button>
                </div>
              </div>
            </div>
          </div>
          <div class="graph-layout">
            <div class="graph-stage">
              <div class="graph-stage-header">
                <div class="graph-stage-copy">
                  <span class="graph-stage-pill" data-i18n-key="graph_theme_legend">Theme Legend</span>
                  <div class="graph-legend">
                    {% for group in graph_groups %}
                    <span class="graph-legend-chip">
                      <span class="graph-legend-dot" style="background: {{ group.color }}"></span>
                      <span data-i18n-label="{{ group.label }}">{{ group.label }}</span>
                      <small>{{ group.count }}</small>
                    </span>
                    {% endfor %}
                  </div>
                </div>
              </div>
              <canvas id="graph-canvas" class="graph-canvas" aria-hidden="true"></canvas>
              <svg id="graph-svg" class="graph-svg" viewBox="0 0 1080 720" role="img" aria-label="Paper relationship graph">{{ initial_graph_svg_html | safe }}</svg>
            </div>
            <aside id="graph-detail" class="graph-detail">
              <p class="eyebrow" data-i18n-key="graph_detail">Graph Detail</p>
              <h2 data-i18n-key="select_node">Select a node</h2>
              <p class="subtle" data-i18n-key="graph_detail_help">{{ graph_detail_help_default }}</p>
            </aside>
          </div>
        </section>
      </main>
    </div>

    <script id="wiki-data" type="application/json">{{ dashboard_data_json | safe }}</script>
    <script id="dashboard-i18n-data" type="application/json">{{ i18n_data_json | safe }}</script>
    <script>
      (() => {
        const data = JSON.parse(document.getElementById("wiki-data").textContent);
        const i18nData = JSON.parse(document.getElementById("dashboard-i18n-data").textContent);
        const searchInput = document.getElementById("search-input");
        const tagChips = document.getElementById("tag-chips");
        const clearFiltersButton = document.getElementById("clear-filters");
        const matchSummary = document.getElementById("match-summary");
        const matchDetail = document.getElementById("match-detail");
        const activeFilters = document.getElementById("active-filters");
        const paperGrid = document.getElementById("paper-grid");
        const databaseGroups = document.getElementById("database-groups");
        const databaseEmpty = document.getElementById("database-empty");
        const databaseSummary = document.getElementById("database-summary");
        const databaseSortSelect = document.getElementById("database-sort");
        const databaseSortDirectionButton = document.getElementById("database-sort-direction");
        const databaseGroupSelect = document.getElementById("database-group");
        const databaseDensitySelect = document.getElementById("database-density");
        const databaseExportButton = document.getElementById("database-export");
        const pageList = document.getElementById("page-list");
        const papersEmpty = document.getElementById("papers-empty");
        const pagesEmpty = document.getElementById("pages-empty");
        const graphCanvas = document.getElementById("graph-canvas");
        const graphSvg = document.getElementById("graph-svg");
        const graphDetail = document.getElementById("graph-detail");
        const graphNodeScaleInput = document.getElementById("graph-node-scale");
        const graphEdgeScaleInput = document.getElementById("graph-edge-scale");
        const graphLabelDensityInput = document.getElementById("graph-label-density");
        const graphRepulsionScaleInput = document.getElementById("graph-repulsion-scale");
        const graphLinkDistanceScaleInput = document.getElementById("graph-link-distance-scale");
        const graphShowLabelsInput = document.getElementById("graph-show-labels");
        const graphNodeScaleValue = document.getElementById("graph-node-scale-value");
        const graphEdgeScaleValue = document.getElementById("graph-edge-scale-value");
        const graphLabelDensityValue = document.getElementById("graph-label-density-value");
        const graphRepulsionScaleValue = document.getElementById("graph-repulsion-scale-value");
        const graphLinkDistanceScaleValue = document.getElementById("graph-link-distance-scale-value");
        const graphShowLabelsValue = document.getElementById("graph-show-labels-value");
        const graphResetButton = document.getElementById("graph-reset-controls");
        const viewButtons = Array.from(document.querySelectorAll(".view-button"));
        const viewStateInputs = Array.from(document.querySelectorAll(".view-state-toggle"));
        const viewStateByView = Object.fromEntries(viewStateInputs.map((input) => [input.dataset.view, input]));
        const langButtons = Array.from(document.querySelectorAll(".lang-button"));

        const pagesById = new Map(data.pages.map((page) => [page.id, page]));
        const SVG_NS = "http://www.w3.org/2000/svg";
        const GRAPH_WIDTH = 1080;
        const GRAPH_HEIGHT = 720;
        const GRAPH_MAX_PIXEL_RATIO = 1.75;
        const GRAPH_TARGET_FPS = 36;
        const GRAPH_ACTIVE_EDGE_BUDGET = 180;
        const GRAPH_SETTINGS_STORAGE_KEY = "paper_atlas_graph_settings_v1";
        const DEFAULT_GRAPH_SETTINGS = Object.freeze({
          nodeScale: 0.72,
          edgeScale: 0.95,
          labelDensity: 0.7,
          repulsionScale: 1,
          linkDistanceScale: 1,
          showLabels: true,
        });
        const DATABASE_SETTINGS_STORAGE_KEY = "paper_atlas_database_settings_v1";
        const DEFAULT_DATABASE_SETTINGS = Object.freeze({
          sortKey: "recent",
          sortDirection: "desc",
          groupKey: "none",
          density: "comfortable",
        });
        const state = {
          search: "",
          tags: new Set(),
          view: "papers",
          selectedNodeId: null,
          language: localStorage.getItem("paper_atlas_lang") || "en",
          graphSettings: loadGraphSettings(),
          databaseSettings: loadDatabaseSettings(),
        };
        let graphRuntime = null;
        let graphBindingsAttached = false;
        let graphCanvasContext = null;
        let graphCanvasPixelRatio = 1;

        function escapeHtml(value) {
          return value
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#39;");
        }

        let localViewerProbe = null;

        function isFileModeNavigation() {
          return window.location.protocol === "file:" || !/^https?:$/.test(window.location.protocol);
        }

        function getLocalViewerOrigin(httpHref) {
          try {
            return new URL(httpHref).origin;
          } catch (_error) {
            return "";
          }
        }

        function canReachLocalViewer(httpHref) {
          const origin = getLocalViewerOrigin(httpHref);
          if (!origin) {
            return Promise.resolve(false);
          }
          if (localViewerProbe && localViewerProbe.origin === origin) {
            return localViewerProbe.promise;
          }
          localViewerProbe = {
            origin,
            promise: new Promise((resolve) => {
              const controller = typeof AbortController === "function" ? new AbortController() : null;
              const timeoutId = window.setTimeout(() => {
                if (controller) {
                  controller.abort();
                }
                resolve(false);
              }, 450);
              fetch(`${origin}/__paper_collect_ping__`, {
                method: "GET",
                cache: "no-store",
                mode: "no-cors",
                signal: controller ? controller.signal : undefined,
              })
                .then(() => {
                  window.clearTimeout(timeoutId);
                  resolve(true);
                })
                .catch(() => {
                  window.clearTimeout(timeoutId);
                  resolve(false);
                });
            }),
          };
          return localViewerProbe.promise;
        }

        async function preferredNavigationTarget(link) {
          const fileHref = link.getAttribute("data-file-href");
          const httpHref = link.getAttribute("data-http-href");
          const href = link.getAttribute("href");
          if (!isFileModeNavigation()) {
            return href || httpHref || fileHref || "#";
          }
          if (httpHref && await canReachLocalViewer(httpHref)) {
            return httpHref;
          }
          return fileHref || href || httpHref || "#";
        }

        function renderHrefAttributes(href, fileHref, httpHref) {
          const safeHref = escapeHtml(href || "#");
          const safeFileHref = fileHref ? ` data-file-href="${escapeHtml(fileHref)}"` : "";
          const safeHttpHref = httpHref ? ` data-http-href="${escapeHtml(httpHref)}"` : "";
          return `href="${safeHref}"${safeFileHref}${safeHttpHref}`;
        }

        function renderExternalHrefAttributes(href) {
          const safeHref = escapeHtml(href || "#");
          return `href="${safeHref}" target="_blank" rel="noreferrer"`;
        }

        document.addEventListener("click", async (event) => {
          const link = event.target.closest ? event.target.closest("a[data-file-href], a[data-http-href]") : null;
          if (!link || !isFileModeNavigation()) {
            return;
          }
          if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
            return;
          }
          event.preventDefault();
          const target = await preferredNavigationTarget(link);
          if (target) {
            window.location.assign(target);
          }
        });

        function t(key) {
          return (i18nData.ui[state.language] || {})[key]
            || (i18nData.ui.en || {})[key]
            || key;
        }

        function translateLabel(label) {
          return (i18nData.labels[state.language] || {})[label]
            || (i18nData.labels.en || {})[label]
            || label;
        }

        function loadGraphSettings() {
          try {
            const parsed = JSON.parse(localStorage.getItem(GRAPH_SETTINGS_STORAGE_KEY) || "{}");
            return {
              nodeScale: clamp(Number(parsed.nodeScale || DEFAULT_GRAPH_SETTINGS.nodeScale), 0.55, 1.4),
              edgeScale: clamp(Number(parsed.edgeScale || DEFAULT_GRAPH_SETTINGS.edgeScale), 0.55, 1.7),
              labelDensity: clamp(Number(parsed.labelDensity || DEFAULT_GRAPH_SETTINGS.labelDensity), 0.35, 1.5),
              repulsionScale: clamp(Number(parsed.repulsionScale || DEFAULT_GRAPH_SETTINGS.repulsionScale), 0.45, 1.8),
              linkDistanceScale: clamp(Number(parsed.linkDistanceScale || DEFAULT_GRAPH_SETTINGS.linkDistanceScale), 0.6, 1.65),
              showLabels: parsed.showLabels !== false,
            };
          } catch (error) {
            return { ...DEFAULT_GRAPH_SETTINGS };
          }
        }

        function saveGraphSettings() {
          localStorage.setItem(GRAPH_SETTINGS_STORAGE_KEY, JSON.stringify(state.graphSettings));
        }

        function loadDatabaseSettings() {
          try {
            const parsed = JSON.parse(localStorage.getItem(DATABASE_SETTINGS_STORAGE_KEY) || "{}");
            const sortKey = ["recent", "year", "title", "section", "status", "relations"].includes(parsed.sortKey)
              ? parsed.sortKey
              : DEFAULT_DATABASE_SETTINGS.sortKey;
            const sortDirection = parsed.sortDirection === "asc" ? "asc" : DEFAULT_DATABASE_SETTINGS.sortDirection;
            const groupKey = ["none", "section", "status", "year", "graph"].includes(parsed.groupKey)
              ? parsed.groupKey
              : DEFAULT_DATABASE_SETTINGS.groupKey;
            const density = parsed.density === "compact" ? "compact" : DEFAULT_DATABASE_SETTINGS.density;
            return { sortKey, sortDirection, groupKey, density };
          } catch (error) {
            return { ...DEFAULT_DATABASE_SETTINGS };
          }
        }

        function saveDatabaseSettings() {
          localStorage.setItem(DATABASE_SETTINGS_STORAGE_KEY, JSON.stringify(state.databaseSettings));
        }

        function syncGraphControlInputs() {
          graphNodeScaleInput.value = String(Math.round(state.graphSettings.nodeScale * 100));
          graphEdgeScaleInput.value = String(Math.round(state.graphSettings.edgeScale * 100));
          graphLabelDensityInput.value = String(Math.round(state.graphSettings.labelDensity * 100));
          graphRepulsionScaleInput.value = String(Math.round(state.graphSettings.repulsionScale * 100));
          graphLinkDistanceScaleInput.value = String(Math.round(state.graphSettings.linkDistanceScale * 100));
          graphShowLabelsInput.checked = state.graphSettings.showLabels;
          graphNodeScaleValue.textContent = `${Math.round(state.graphSettings.nodeScale * 100)}%`;
          graphEdgeScaleValue.textContent = `${Math.round(state.graphSettings.edgeScale * 100)}%`;
          graphLabelDensityValue.textContent = `${Math.round(state.graphSettings.labelDensity * 100)}%`;
          graphRepulsionScaleValue.textContent = `${Math.round(state.graphSettings.repulsionScale * 100)}%`;
          graphLinkDistanceScaleValue.textContent = `${Math.round(state.graphSettings.linkDistanceScale * 100)}%`;
          graphShowLabelsValue.textContent = state.graphSettings.showLabels ? t("graph_toggle_on") : t("graph_toggle_off");
        }

        function syncDatabaseControlInputs() {
          databaseSortSelect.value = state.databaseSettings.sortKey;
          databaseGroupSelect.value = state.databaseSettings.groupKey;
          databaseDensitySelect.value = state.databaseSettings.density;
          databaseSortDirectionButton.textContent = state.databaseSettings.sortDirection === "asc" ? "↑" : "↓";
        }

        function applyLanguage() {
          document.documentElement.lang = state.language === "ko" ? "ko" : "en";
          document.querySelectorAll("[data-i18n-key]").forEach((element) => {
            element.textContent = t(element.dataset.i18nKey);
          });
          document.querySelectorAll("[data-i18n-title]").forEach((element) => {
            const label = t(element.dataset.i18nTitle);
            element.setAttribute("title", label);
            element.setAttribute("aria-label", label);
          });
          document.querySelectorAll("[data-i18n-placeholder]").forEach((element) => {
            element.setAttribute("placeholder", t(element.dataset.i18nPlaceholder));
          });
          document.querySelectorAll("[data-i18n-label]").forEach((element) => {
            element.textContent = translateLabel(element.dataset.i18nLabel);
          });
          langButtons.forEach((button) => {
            button.classList.toggle("active", button.dataset.lang === state.language);
          });
          syncGraphControlInputs();
          syncDatabaseControlInputs();
        }

        function filteredPages() {
          const query = state.search.trim().toLowerCase();
          return data.pages.filter((page) => {
            if (query && !page.search_text.includes(query)) {
              return false;
            }
            if (!state.tags.size) {
              return true;
            }
            return Array.from(state.tags).every((tag) => page.tags_norm.includes(tag));
          });
        }

        function filteredPapers() {
          return filteredPages()
            .filter((page) => page.section === "sources")
            .sort((a, b) => {
              const aYear = a.year || 0;
              const bYear = b.year || 0;
              if (aYear !== bYear) {
                return bYear - aYear;
              }
              return a.title.localeCompare(b.title);
            });
        }

        function pageStatusLabel(page) {
          return page.status || t("database_unspecified");
        }

        function pageThemeLabel(page) {
          return page.graph_group || t("database_group_untitled");
        }

        function pageYearLabel(page) {
          return page.year ? String(page.year) : t("database_unspecified");
        }

        function databaseGroupLabel(groupKey, page) {
          if (groupKey === "section") {
            return translateLabel(page.section_label);
          }
          if (groupKey === "status") {
            return translateLabel(pageStatusLabel(page));
          }
          if (groupKey === "year") {
            return pageYearLabel(page);
          }
          if (groupKey === "graph") {
            return translateLabel(pageThemeLabel(page));
          }
          return t("database_group_untitled");
        }

        function databaseSortValue(page, sortKey) {
          if (sortKey === "year") {
            return page.year || 0;
          }
          if (sortKey === "section") {
            return page.section_label;
          }
          if (sortKey === "status") {
            return pageStatusLabel(page);
          }
          if (sortKey === "relations") {
            return page.relation_count || 0;
          }
          if (sortKey === "recent") {
            return page.sort_timestamp || 0;
          }
          return page.title;
        }

        function compareDatabasePages(left, right) {
          const sortKey = state.databaseSettings.sortKey;
          const direction = state.databaseSettings.sortDirection === "asc" ? 1 : -1;
          const leftValue = databaseSortValue(left, sortKey);
          const rightValue = databaseSortValue(right, sortKey);

          let comparison = 0;
          if (typeof leftValue === "number" && typeof rightValue === "number") {
            comparison = leftValue - rightValue;
          } else {
            comparison = String(leftValue).localeCompare(String(rightValue));
          }

          if (comparison === 0) {
            comparison = left.title.localeCompare(right.title);
          }
          return comparison * direction;
        }

        function databaseRows() {
          return [...filteredPages()].sort(compareDatabasePages);
        }

        function renderTagChips() {
          tagChips.innerHTML = data.tags
            .map((tag) => {
              const active = state.tags.has(tag.slug) ? " active" : "";
              return `
                <button class="tag-chip${active}" type="button" data-tag="${escapeHtml(tag.slug)}">
                  <span>${escapeHtml(translateLabel(tag.label))}</span>
                  <small>${tag.count}</small>
                </button>
              `;
            })
            .join("");

          tagChips.querySelectorAll(".tag-chip").forEach((button) => {
            button.addEventListener("click", () => {
              const slug = button.dataset.tag;
              if (state.tags.has(slug)) {
                state.tags.delete(slug);
              } else {
                state.tags.add(slug);
              }
              renderAll();
            });
          });
        }

        function renderActiveFilters() {
          const tagBits = Array.from(state.tags)
            .map((slug) => data.tags.find((tag) => tag.slug === slug))
            .filter(Boolean)
            .map((tag) => `<span class="active-chip">${escapeHtml(translateLabel(tag.label))}</span>`);

          const searchBit = state.search
            ? `<span class="active-chip">${escapeHtml(t("search_prefix"))}: ${escapeHtml(state.search)}</span>`
            : "";

          activeFilters.innerHTML = [searchBit, ...tagBits].filter(Boolean).join("");
        }

        function renderCounts() {
          const pages = filteredPages();
          const papers = pages.filter((page) => page.section === "sources");
          if (state.language === "ko") {
            matchSummary.textContent = `논문 ${papers.length}편, 페이지 ${pages.length}개가 일치합니다`;
          } else {
            matchSummary.textContent = `${papers.length} papers and ${pages.length} pages match`;
          }
          matchDetail.textContent = t("match_detail");
        }

        function renderPapers() {
          const papers = filteredPapers();
          papersEmpty.classList.toggle("hidden", papers.length !== 0);
          paperGrid.innerHTML = papers
            .map((paper) => {
              const tagHtml = paper.tags
                .slice(0, 8)
                .map((tag) => `<span class="mini-chip">${escapeHtml(translateLabel(tag))}</span>`)
                .join("");

              const pdfLink = paper.pdf_href
                ? `<a class="card-link secondary" ${renderHrefAttributes(paper.pdf_href, paper.pdf_file_href, paper.pdf_http_href)}>${escapeHtml(t("open_pdf"))}</a>`
                : "";
              const articleLink = paper.article_href
                ? `<a class="card-link tertiary" ${renderExternalHrefAttributes(paper.article_href)}>${escapeHtml(t("open_article"))}</a>`
                : "";

              return `
                <article class="paper-card">
                  <div class="card-topline">
                    <span class="section-pill section-${escapeHtml(paper.section || "core")}">${escapeHtml(translateLabel(paper.section_label))}</span>
                    <span class="year-pill">${paper.year || ""}</span>
                  </div>
                  <h2>${escapeHtml(paper.title)}</h2>
                  <p class="card-excerpt">${escapeHtml(paper.excerpt)}</p>
                  <div class="card-tags">${tagHtml}</div>
                  <div class="card-actions">
                    <a class="card-link" ${renderHrefAttributes(paper.href, paper.file_href, paper.http_href)}>${escapeHtml(t("open_page"))}</a>
                    ${articleLink}
                    ${pdfLink}
                  </div>
                </article>
              `;
            })
            .join("");
        }

        function renderPages() {
          const pages = filteredPages().sort((a, b) => {
            if (a.section_label !== b.section_label) {
              return a.section_label.localeCompare(b.section_label);
            }
            return a.title.localeCompare(b.title);
          });

          pagesEmpty.classList.toggle("hidden", pages.length !== 0);
          pageList.innerHTML = pages
            .map((page) => {
              const tagHtml = page.tags
                .slice(0, 6)
                .map((tag) => `<span class="mini-chip">${escapeHtml(translateLabel(tag))}</span>`)
                .join("");
              return `
                <article class="page-row">
                  <div class="page-row-main">
                    <div class="page-row-head">
                      <span class="section-pill section-${escapeHtml(page.section || "core")}">${escapeHtml(translateLabel(page.section_label))}</span>
                      <a class="page-row-link" ${renderHrefAttributes(page.href, page.file_href, page.http_href)}>${escapeHtml(page.title)}</a>
                    </div>
                    <p class="page-row-excerpt">${escapeHtml(page.excerpt)}</p>
                    <div class="card-tags">${tagHtml}</div>
                  </div>
                  <div class="page-row-actions">
                    <a class="card-link" ${renderHrefAttributes(page.href, page.file_href, page.http_href)}>${escapeHtml(t("open"))}</a>
                  </div>
                </article>
              `;
            })
            .join("");
        }

        function databaseSummaryMetrics(rows) {
          const papers = rows.filter((page) => page.section === "sources").length;
          const years = rows.map((page) => page.year).filter(Boolean);
          const groups = new Set();
          if (state.databaseSettings.groupKey !== "none") {
            rows.forEach((page) => groups.add(databaseGroupLabel(state.databaseSettings.groupKey, page)));
          }
          return {
            rows: rows.length,
            papers,
            yearRange: years.length
              ? `${Math.min(...years)}-${Math.max(...years)}`
              : t("database_unspecified"),
            groups: groups.size || 1,
          };
        }

        function renderDatabaseSummary(rows) {
          const metrics = databaseSummaryMetrics(rows);
          databaseSummary.innerHTML = `
            <span class="summary-chip"><strong>${metrics.rows}</strong><span>${escapeHtml(t("database_summary_rows"))}</span></span>
            <span class="summary-chip"><strong>${metrics.papers}</strong><span>${escapeHtml(t("database_summary_papers"))}</span></span>
            <span class="summary-chip"><strong>${escapeHtml(metrics.yearRange)}</strong><span>${escapeHtml(t("database_summary_years"))}</span></span>
            <span class="summary-chip"><strong>${metrics.groups}</strong><span>${escapeHtml(t("database_summary_groups"))}</span></span>
          `;
        }

        function renderDatabaseTable(rows) {
          const densityClass = state.databaseSettings.density === "compact" ? " compact" : "";
          const rowHtml = rows
            .map((page) => {
              const tags = page.tags
                .slice(0, 4)
                .map((tag) => `<span class="mini-chip">${escapeHtml(translateLabel(tag))}</span>`)
                .join("");
              const pdfLink = page.pdf_href
                ? `<a class="table-action secondary" ${renderHrefAttributes(page.pdf_href, page.pdf_file_href, page.pdf_http_href)}>${escapeHtml(t("open_pdf"))}</a>`
                : "";
              const articleLink = page.article_href
                ? `<a class="table-action tertiary" ${renderExternalHrefAttributes(page.article_href)}>${escapeHtml(t("open_article"))}</a>`
                : "";
              return `
                <tr>
                  <td class="database-title-cell">
                    <a class="database-title-link" ${renderHrefAttributes(page.href, page.file_href, page.http_href)}>${escapeHtml(page.title)}</a>
                    <p class="database-subtle">${escapeHtml(page.excerpt)}</p>
                  </td>
                  <td><span class="section-pill section-${escapeHtml(page.section || "core")}">${escapeHtml(translateLabel(page.section_label))}</span></td>
                  <td>${escapeHtml(pageYearLabel(page))}</td>
                  <td>${escapeHtml(translateLabel(pageStatusLabel(page)))}</td>
                  <td>${escapeHtml(translateLabel(pageThemeLabel(page)))}</td>
                  <td>${page.relation_count || 0}</td>
                  <td><div class="database-tag-cell">${tags}</div></td>
                  <td>
                    <div class="database-actions">
                      <a class="table-action" ${renderHrefAttributes(page.href, page.file_href, page.http_href)}>${escapeHtml(t("open"))}</a>
                      ${articleLink}
                      ${pdfLink}
                    </div>
                  </td>
                </tr>
              `;
            })
            .join("");

          return `
            <div class="database-table-wrap${densityClass}">
              <table class="database-table">
                <thead>
                  <tr>
                    <th data-i18n-key="database_column_title">${escapeHtml(t("database_column_title"))}</th>
                    <th data-i18n-key="database_column_section">${escapeHtml(t("database_column_section"))}</th>
                    <th data-i18n-key="database_column_year">${escapeHtml(t("database_column_year"))}</th>
                    <th data-i18n-key="database_column_status">${escapeHtml(t("database_column_status"))}</th>
                    <th data-i18n-key="database_column_theme">${escapeHtml(t("database_column_theme"))}</th>
                    <th data-i18n-key="database_column_relations">${escapeHtml(t("database_column_relations"))}</th>
                    <th data-i18n-key="database_column_tags">${escapeHtml(t("database_column_tags"))}</th>
                    <th data-i18n-key="database_column_actions">${escapeHtml(t("database_column_actions"))}</th>
                  </tr>
                </thead>
                <tbody>${rowHtml}</tbody>
              </table>
            </div>
          `;
        }

        function renderDatabase() {
          const rows = databaseRows();
          renderDatabaseSummary(rows);
          databaseEmpty.classList.toggle("hidden", rows.length !== 0);
          if (!rows.length) {
            databaseGroups.innerHTML = "";
            return;
          }

          const grouped = new Map();
          if (state.databaseSettings.groupKey === "none") {
            grouped.set("", rows);
          } else {
            rows.forEach((page) => {
              const groupLabel = databaseGroupLabel(state.databaseSettings.groupKey, page);
              if (!grouped.has(groupLabel)) {
                grouped.set(groupLabel, []);
              }
              grouped.get(groupLabel).push(page);
            });
          }

          databaseGroups.innerHTML = Array.from(grouped.entries())
            .map(([label, groupRows]) => {
              const header = state.databaseSettings.groupKey === "none"
                ? ""
                : `
                  <div class="database-group-header">
                    <div>
                      <p class="eyebrow">${escapeHtml(t("database_group"))}</p>
                      <h3>${escapeHtml(label)}</h3>
                    </div>
                    <span class="summary-chip subtle-chip"><strong>${groupRows.length}</strong><span>${escapeHtml(t("database_summary_rows"))}</span></span>
                  </div>
                `;
              return `<section class="database-group">${header}${renderDatabaseTable(groupRows)}</section>`;
            })
            .join("");
        }

        function exportDatabaseCsv() {
          const rows = databaseRows();
          const lines = [
            [
              t("database_column_title"),
              t("database_column_section"),
              t("database_column_year"),
              t("database_column_status"),
              t("database_column_theme"),
              t("database_column_relations"),
              t("database_column_tags"),
              "URL",
              "PDF",
            ],
            ...rows.map((page) => [
              page.title,
              translateLabel(page.section_label),
              pageYearLabel(page),
              translateLabel(pageStatusLabel(page)),
              translateLabel(pageThemeLabel(page)),
              String(page.relation_count || 0),
              page.tags.join(" | "),
              page.http_href || page.file_href || page.href,
              page.pdf_http_href || page.pdf_file_href || page.pdf_href || "",
            ]),
          ];

          const csv = lines
            .map((row) => row.map((value) => `"${String(value).replace(/"/g, '""')}"`).join(","))
            .join("\\n");
          const blob = new Blob(["\\ufeff" + csv], { type: "text/csv;charset=utf-8;" });
          const url = URL.createObjectURL(blob);
          const link = document.createElement("a");
          const fileStem = `${t("database_export_filename")}-${new Date().toISOString().slice(0, 10)}.csv`;
          link.href = url;
          link.download = fileStem;
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
          URL.revokeObjectURL(url);
        }

        function clamp(value, min, max) {
          return Math.min(max, Math.max(min, value));
        }

        function hashString(value) {
          let hash = 0;
          for (let index = 0; index < value.length; index += 1) {
            hash = ((hash << 5) - hash) + value.charCodeAt(index);
            hash |= 0;
          }
          return Math.abs(hash);
        }

        function createSvgElement(name, attributes = {}) {
          const element = document.createElementNS(SVG_NS, name);
          Object.entries(attributes).forEach(([key, value]) => {
            element.setAttribute(key, String(value));
          });
          return element;
        }

        function configureGraphCanvas() {
          if (!graphCanvas) {
            return null;
          }
          if (!graphCanvasContext) {
            graphCanvasContext = graphCanvas.getContext("2d", { alpha: true, desynchronized: true })
              || graphCanvas.getContext("2d");
          }
          if (!graphCanvasContext) {
            return null;
          }
          const nextPixelRatio = clamp(window.devicePixelRatio || 1, 1, GRAPH_MAX_PIXEL_RATIO);
          const targetWidth = Math.round(GRAPH_WIDTH * nextPixelRatio);
          const targetHeight = Math.round(GRAPH_HEIGHT * nextPixelRatio);
          if (
            graphCanvas.width !== targetWidth
            || graphCanvas.height !== targetHeight
            || graphCanvasPixelRatio !== nextPixelRatio
          ) {
            graphCanvas.width = targetWidth;
            graphCanvas.height = targetHeight;
            graphCanvasPixelRatio = nextPixelRatio;
          }
          return graphCanvasContext;
        }

        function clearGraphCanvas() {
          const context = configureGraphCanvas();
          if (!context) {
            return;
          }
          context.setTransform(graphCanvasPixelRatio, 0, 0, graphCanvasPixelRatio, 0, 0);
          context.clearRect(0, 0, GRAPH_WIDTH, GRAPH_HEIGHT);
        }

        function currentGraphNodeRadius(node) {
          return Math.max(4.2, node.baseRadius * state.graphSettings.nodeScale);
        }

        function currentGraphEdgeWidth(edge) {
          const baseWidth = 0.8 + Math.min(edge.strength || 1, 7) * 0.42;
          return baseWidth * state.graphSettings.edgeScale;
        }

        function currentGraphIdealLength(edge) {
          return edge.baseIdealLength * state.graphSettings.linkDistanceScale;
        }

        function colorWithAlpha(color, alpha) {
          if (!color) {
            return `rgba(122, 53, 32, ${alpha})`;
          }
          const normalized = color.replace("#", "");
          if (normalized.length !== 6) {
            return color;
          }
          const red = parseInt(normalized.slice(0, 2), 16);
          const green = parseInt(normalized.slice(2, 4), 16);
          const blue = parseInt(normalized.slice(4, 6), 16);
          return `rgba(${red}, ${green}, ${blue}, ${alpha})`;
        }

        function drawRoundedRect(context, x, y, width, height, radius) {
          const safeRadius = Math.min(radius, width / 2, height / 2);
          context.beginPath();
          context.moveTo(x + safeRadius, y);
          context.lineTo(x + width - safeRadius, y);
          context.quadraticCurveTo(x + width, y, x + width, y + safeRadius);
          context.lineTo(x + width, y + height - safeRadius);
          context.quadraticCurveTo(x + width, y + height, x + width - safeRadius, y + height);
          context.lineTo(x + safeRadius, y + height);
          context.quadraticCurveTo(x, y + height, x, y + height - safeRadius);
          context.lineTo(x, y + safeRadius);
          context.quadraticCurveTo(x, y, x + safeRadius, y);
          context.closePath();
        }

        function drawGraphLabel(context, text, x, y) {
          context.font = "10.5px Arial, 'Malgun Gothic', 'Apple SD Gothic Neo', 'Noto Sans KR', sans-serif";
          const metrics = context.measureText(text);
          const paddingX = 8;
          const width = metrics.width + paddingX * 2;
          const height = 22;
          const left = x - width / 2;
          const top = y;
          context.save();
          drawRoundedRect(context, left, top, width, height, 11);
          context.fillStyle = "rgba(255, 252, 247, 0.92)";
          context.fill();
          context.strokeStyle = "rgba(77, 60, 44, 0.1)";
          context.lineWidth = 1;
          context.stroke();
          context.fillStyle = "#3b3028";
          context.textAlign = "center";
          context.textBaseline = "middle";
          context.fillText(text, x, top + height / 2 + 0.5);
          context.restore();
        }

        function stopGraphAnimation(clearScene = false) {
          if (graphRuntime && graphRuntime.rafId) {
            cancelAnimationFrame(graphRuntime.rafId);
          }
          if (graphRuntime) {
            graphRuntime.rafId = 0;
            graphRuntime.draggingNode = null;
            graphRuntime.panning = null;
          }
          if (clearScene) {
            graphSvg.innerHTML = "";
            clearGraphCanvas();
          }
          graphSvg.classList.remove("panning", "dragging");
          graphRuntime = clearScene ? null : graphRuntime;
        }

        function computeGraphAnchors(nodes) {
          const labels = data.graph_groups
            .filter((group) => nodes.some((node) => node.graph_group === group.label))
            .map((group) => group.label);

          const anchors = new Map();
          if (labels.length <= 1) {
            anchors.set(labels[0] || "Other Papers", { x: GRAPH_WIDTH / 2, y: GRAPH_HEIGHT / 2 });
            return anchors;
          }

          const columns = Math.max(2, Math.ceil(Math.sqrt(labels.length)));
          const rows = Math.max(1, Math.ceil(labels.length / columns));
          const xSpacing = GRAPH_WIDTH / (columns + 1);
          const ySpacing = GRAPH_HEIGHT / (rows + 1);
          labels.forEach((label, index) => {
            const row = Math.floor(index / columns);
            const column = index % columns;
            const rowOffset = row % 2 === 0 ? 0 : xSpacing * 0.18;
            anchors.set(label, {
              x: clamp(xSpacing * (column + 1) + rowOffset, 140, GRAPH_WIDTH - 140),
              y: clamp(ySpacing * (row + 1), 120, GRAPH_HEIGHT - 120),
            });
          });
          return anchors;
        }

        function graphLayoutKey(visiblePages, visibleEdges) {
          const nodePart = visiblePages.map((page) => page.id).join("|");
          const edgePart = visibleEdges.map((edge) => `${edge.source}->${edge.target}:${edge.strength || 1}`).join("|");
          return `${nodePart}__${edgePart}`;
        }

        function graphNodeAtPoint(point) {
          if (!graphRuntime) {
            return null;
          }
          for (let index = graphRuntime.nodes.length - 1; index >= 0; index -= 1) {
            const node = graphRuntime.nodes[index];
            const radius = currentGraphNodeRadius(node) + 3;
            const dx = point.x - node.x;
            const dy = point.y - node.y;
            if ((dx * dx) + (dy * dy) <= radius * radius) {
              return node;
            }
          }
          return null;
        }

        function ensureGraphBindings() {
          if (graphBindingsAttached) {
            return;
          }
          graphBindingsAttached = true;

          graphSvg.addEventListener("pointerdown", (event) => {
            if (!graphRuntime) {
              return;
            }
            const point = graphPointFromEvent(event);
            const hitNode = graphNodeAtPoint(point);
            if (hitNode) {
              graphRuntime.draggingNode = { node: hitNode, pointerId: event.pointerId, moved: false };
              graphRuntime.pointerJustMoved = false;
              hitNode.fx = hitNode.x;
              hitNode.fy = hitNode.y;
              graphSvg.classList.add("dragging");
              if (graphSvg.setPointerCapture) {
                graphSvg.setPointerCapture(event.pointerId);
              }
              kickGraphSimulation();
              return;
            }
            graphRuntime.panning = {
              pointerId: event.pointerId,
              startX: event.clientX,
              startY: event.clientY,
              originX: graphRuntime.transform.x,
              originY: graphRuntime.transform.y,
            };
            graphRuntime.pointerJustMoved = false;
            graphSvg.classList.add("panning");
            if (graphSvg.setPointerCapture) {
              graphSvg.setPointerCapture(event.pointerId);
            }
          });

          graphSvg.addEventListener("pointermove", (event) => {
            if (!graphRuntime) {
              return;
            }

            if (graphRuntime.draggingNode && graphRuntime.draggingNode.pointerId === event.pointerId) {
              const point = graphPointFromEvent(event);
              graphRuntime.draggingNode.node.fx = point.x;
              graphRuntime.draggingNode.node.fy = point.y;
              graphRuntime.draggingNode.node.x = point.x;
              graphRuntime.draggingNode.node.y = point.y;
              graphRuntime.draggingNode.node.vx = 0;
              graphRuntime.draggingNode.node.vy = 0;
              graphRuntime.draggingNode.moved = true;
              graphRuntime.pointerJustMoved = true;
              kickGraphSimulation();
              return;
            }

            if (graphRuntime.panning && graphRuntime.panning.pointerId === event.pointerId) {
              const rect = graphSvg.getBoundingClientRect();
              const scaleX = GRAPH_WIDTH / rect.width;
              const scaleY = GRAPH_HEIGHT / rect.height;
              graphRuntime.transform.x = graphRuntime.panning.originX + (event.clientX - graphRuntime.panning.startX) * scaleX;
              graphRuntime.transform.y = graphRuntime.panning.originY + (event.clientY - graphRuntime.panning.startY) * scaleY;
              graphRuntime.pointerJustMoved = true;
              updateGraphTransform();
              return;
            }

            const point = graphPointFromEvent(event);
            graphSvg.style.cursor = graphNodeAtPoint(point) ? "pointer" : "grab";
          });

          graphSvg.addEventListener("pointerup", (event) => {
            finishGraphPointer(event);
          });

          graphSvg.addEventListener("pointerleave", (event) => {
            if (event.buttons === 0) {
              finishGraphPointer(event);
            }
          });

          graphSvg.addEventListener("wheel", (event) => {
            if (!graphRuntime || state.view !== "graph") {
              return;
            }
            event.preventDefault();
            const rect = graphSvg.getBoundingClientRect();
            const svgX = (event.clientX - rect.left) * (GRAPH_WIDTH / rect.width);
            const svgY = (event.clientY - rect.top) * (GRAPH_HEIGHT / rect.height);
            const before = {
              x: (svgX - graphRuntime.transform.x) / graphRuntime.transform.k,
              y: (svgY - graphRuntime.transform.y) / graphRuntime.transform.k,
            };
            const zoomFactor = event.deltaY < 0 ? 1.08 : 0.92;
            const nextScale = clamp(graphRuntime.transform.k * zoomFactor, 0.56, 2.75);
            graphRuntime.transform.k = nextScale;
            graphRuntime.transform.x = svgX - before.x * nextScale;
            graphRuntime.transform.y = svgY - before.y * nextScale;
            updateGraphTransform();
          }, { passive: false });
        }

        function finishGraphPointer(event) {
          if (!graphRuntime) {
            return;
          }

          if (graphRuntime.draggingNode && graphRuntime.draggingNode.pointerId === event.pointerId) {
            const dragged = graphRuntime.draggingNode;
            if (!dragged.moved) {
              state.selectedNodeId = dragged.node.id;
              updateGraphScene();
              renderGraphDetail(pagesById.get(state.selectedNodeId));
            }
            dragged.node.fx = null;
            dragged.node.fy = null;
            graphRuntime.draggingNode = null;
          }

          if (graphRuntime.panning && graphRuntime.panning.pointerId === event.pointerId) {
            graphRuntime.panning = null;
          }

          graphSvg.classList.remove("panning", "dragging");
          if (graphSvg.releasePointerCapture && graphSvg.hasPointerCapture && graphSvg.hasPointerCapture(event.pointerId)) {
            graphSvg.releasePointerCapture(event.pointerId);
          }
        }

        function graphPointFromEvent(event) {
          const rect = graphSvg.getBoundingClientRect();
          const svgX = (event.clientX - rect.left) * (GRAPH_WIDTH / rect.width);
          const svgY = (event.clientY - rect.top) * (GRAPH_HEIGHT / rect.height);
          return {
            x: (svgX - graphRuntime.transform.x) / graphRuntime.transform.k,
            y: (svgY - graphRuntime.transform.y) / graphRuntime.transform.k,
          };
        }

        function createGraphRuntime(visiblePages, visibleEdges) {
          const degrees = new Map();
          visiblePages.forEach((page) => degrees.set(page.id, 0));
          visibleEdges.forEach((edge) => {
            degrees.set(edge.source, (degrees.get(edge.source) || 0) + (edge.strength || 1));
            degrees.set(edge.target, (degrees.get(edge.target) || 0) + (edge.strength || 1));
          });

          const anchors = computeGraphAnchors(visiblePages);
          const nodes = visiblePages.map((page) => {
            const anchor = anchors.get(page.graph_group) || { x: GRAPH_WIDTH / 2, y: GRAPH_HEIGHT / 2 };
            const hash = hashString(page.id);
            const jitterRadius = 18 + (hash % 33);
            const angle = ((hash % 360) * Math.PI) / 180;
            const degree = degrees.get(page.id) || 0;
            return {
              id: page.id,
              page,
              graph_group: page.graph_group,
              degree,
              baseRadius: 6 + Math.min(5, Math.sqrt(Math.max(degree, 1)) * 1.2),
              x: anchor.x + Math.cos(angle) * jitterRadius,
              y: anchor.y + Math.sin(angle) * jitterRadius,
              vx: 0,
              vy: 0,
              fx: null,
              fy: null,
            };
          });

          const nodeById = new Map(nodes.map((node) => [node.id, node]));
          const adjacency = new Map(nodes.map((node) => [node.id, new Set([node.id])]));
          const edges = visibleEdges
            .map((edge) => ({
              ...edge,
              sourceNode: nodeById.get(edge.source),
              targetNode: nodeById.get(edge.target),
              baseIdealLength: 152 - Math.min((edge.strength || 1), 6) * 12,
              stiffness: 0.0038 + Math.min((edge.strength || 1), 6) * 0.0011,
            }))
            .filter((edge) => edge.sourceNode && edge.targetNode);

          edges.forEach((edge) => {
            adjacency.get(edge.source)?.add(edge.target);
            adjacency.get(edge.target)?.add(edge.source);
          });

          return {
            key: graphLayoutKey(visiblePages, visibleEdges),
            nodes,
            edges,
            drawEdges: [...edges].sort((left, right) => {
              if ((right.strength || 1) !== (left.strength || 1)) {
                return (right.strength || 1) - (left.strength || 1);
              }
              return `${left.source}-${left.target}`.localeCompare(`${right.source}-${right.target}`);
            }),
            adjacency,
            anchors,
            transform: { x: 0, y: 0, k: 1 },
            draggingNode: null,
            panning: null,
            pointerJustMoved: false,
            rafId: 0,
            settledFrames: 0,
            lastFrameTime: 0,
            scene: null,
          };
        }

        function updateGraphTransform() {
          if (!graphRuntime) {
            return;
          }
          drawGraphScene();
        }

        function initializeGraphScene() {
          if (!graphRuntime) {
            return;
          }

          graphSvg.innerHTML = "";
          graphSvg.setAttribute("viewBox", `0 0 ${GRAPH_WIDTH} ${GRAPH_HEIGHT}`);
          clearGraphCanvas();
          ensureGraphBindings();

          graphRuntime.scene = {};
          updateGraphTransform();
          updateGraphScene();
        }

        function connectedIds(nodeId) {
          if (!graphRuntime) {
            return new Set([nodeId]);
          }
          return new Set(graphRuntime.adjacency.get(nodeId) || [nodeId]);
        }

        function drawGraphScene() {
          if (!graphRuntime) {
            clearGraphCanvas();
            return;
          }

          const context = configureGraphCanvas();
          if (!context) {
            return;
          }

          const selectedId = state.selectedNodeId;
          context.setTransform(graphCanvasPixelRatio, 0, 0, graphCanvasPixelRatio, 0, 0);
          context.clearRect(0, 0, GRAPH_WIDTH, GRAPH_HEIGHT);
          context.save();
          context.translate(graphRuntime.transform.x, graphRuntime.transform.y);
          context.scale(graphRuntime.transform.k, graphRuntime.transform.k);
          context.lineCap = "round";

          const isInteractionActive = Boolean(graphRuntime.draggingNode || graphRuntime.panning);
          const isActiveMotion = Boolean(isInteractionActive || graphRuntime.rafId);
          const relatedIds = selectedId ? connectedIds(selectedId) : new Set();
          const labelIds = visibleGraphLabelIds();
          let edgesToDraw = graphRuntime.edges;
          if (isActiveMotion && graphRuntime.drawEdges.length > GRAPH_ACTIVE_EDGE_BUDGET) {
            const relatedEdges = [];
            const otherEdges = [];
            graphRuntime.drawEdges.forEach((edge) => {
              const related = selectedId && (edge.source === selectedId || edge.target === selectedId);
              if (related) {
                relatedEdges.push(edge);
              } else {
                otherEdges.push(edge);
              }
            });
            const remainingBudget = Math.max(0, GRAPH_ACTIVE_EDGE_BUDGET - relatedEdges.length);
            edgesToDraw = relatedEdges.concat(otherEdges.slice(0, remainingBudget));
          }

          edgesToDraw.forEach((edge) => {
            const related = selectedId && (edge.source === selectedId || edge.target === selectedId);
            const dimmed = selectedId && !related;
            const edgeColor = related
              ? colorWithAlpha(edge.sourceNode.page.graph_color || "#8e3c27", 0.44)
              : colorWithAlpha(edge.sourceNode.page.graph_color || "#8e3c27", 0.18);
            context.beginPath();
            context.moveTo(edge.sourceNode.x, edge.sourceNode.y);
            context.lineTo(edge.targetNode.x, edge.targetNode.y);
            context.lineWidth = currentGraphEdgeWidth(edge);
            context.strokeStyle = edgeColor;
            context.globalAlpha = dimmed ? 0.12 : Math.min(0.22 + (edge.strength || 1) * 0.08, 0.82);
            context.stroke();
          });

          graphRuntime.nodes.forEach((node) => {
            const radius = currentGraphNodeRadius(node);
            const selected = selectedId === node.id;
            const dimmed = selectedId && !relatedIds.has(node.id);
            const nodeColor = node.page.graph_color || "#8e3c27";
            context.globalAlpha = dimmed ? 0.28 : 1;
            context.shadowColor = colorWithAlpha(nodeColor, selected ? 0.34 : 0.16);
            context.shadowBlur = selected ? 18 : 10;
            context.shadowOffsetX = 0;
            context.shadowOffsetY = selected ? 6 : 3;
            context.beginPath();
            context.arc(node.x, node.y, radius, 0, Math.PI * 2);
            context.fillStyle = nodeColor;
            context.fill();
            context.shadowBlur = 0;
            context.shadowOffsetX = 0;
            context.shadowOffsetY = 0;
            context.lineWidth = selected ? 3 : 2;
            context.strokeStyle = "rgba(255, 255, 255, 0.82)";
            context.stroke();
            if (selected) {
              context.beginPath();
              context.arc(node.x, node.y, radius + 6, 0, Math.PI * 2);
              context.lineWidth = 1.6;
              context.strokeStyle = colorWithAlpha(nodeColor, 0.36);
              context.stroke();
            }

            if (state.graphSettings.showLabels && (labelIds.has(node.id) || selected) && !isInteractionActive) {
              drawGraphLabel(context, node.page.short_title, node.x, node.y + radius + 8);
            }
          });

          context.restore();
          context.globalAlpha = 1;
        }

        function visibleGraphLabelIds() {
          if (!graphRuntime) {
            return new Set();
          }
          if (!state.graphSettings.showLabels) {
            return new Set();
          }

          const nodesByDegree = [...graphRuntime.nodes].sort((left, right) => {
            if (left.degree !== right.degree) {
              return right.degree - left.degree;
            }
            return left.page.title.localeCompare(right.page.title);
          });

          const baseLimit = graphRuntime.nodes.length > 24
            ? 8
            : Math.max(6, Math.ceil(graphRuntime.nodes.length * 0.68));
          const limit = clamp(
            Math.round(baseLimit * state.graphSettings.labelDensity),
            3,
            graphRuntime.nodes.length,
          );
          const visibleIds = new Set(nodesByDegree.slice(0, limit).map((node) => node.id));
          if (state.selectedNodeId) {
            connectedIds(state.selectedNodeId).forEach((id) => visibleIds.add(id));
          }
          return visibleIds;
        }

        function updateGraphScene() {
          if (!graphRuntime) {
            return;
          }
          drawGraphScene();
        }

        function graphSettingsNeedRebuild(previousSettings, nextSettings) {
          return previousSettings.repulsionScale !== nextSettings.repulsionScale
            || previousSettings.linkDistanceScale !== nextSettings.linkDistanceScale;
        }

        function isGraphVisible() {
          const graphView = document.getElementById("graph-view");
          if (!graphView) {
            return false;
          }
          if (viewStateByView.graph && viewStateByView.graph.checked) {
            return true;
          }
          if (!graphView.classList.contains("hidden")) {
            return true;
          }
          return window.getComputedStyle(graphView).display !== "none";
        }

        function rebuildGraphRuntime() {
          const visiblePages = filteredPapers();
          const visibleIds = new Set(visiblePages.map((page) => page.id));
          const visibleEdges = data.paper_edges.filter((edge) => visibleIds.has(edge.source) && visibleIds.has(edge.target));
          const previousTransform = graphRuntime ? { ...graphRuntime.transform } : { x: 0, y: 0, k: 1 };
          const previousPositions = new Map(
            graphRuntime
              ? graphRuntime.nodes.map((node) => [node.id, { x: node.x, y: node.y }])
              : [],
          );

          stopGraphAnimation(true);
          graphRuntime = createGraphRuntime(visiblePages, visibleEdges);
          graphRuntime.transform = previousTransform;
          graphRuntime.nodes.forEach((node) => {
            const previous = previousPositions.get(node.id);
            if (!previous) {
              return;
            }
            node.x = previous.x;
            node.y = previous.y;
          });
          initializeGraphScene();
          kickGraphSimulation();
        }

        function refreshGraphFromControls(forceRebuild = false) {
          if (!isGraphVisible()) {
            return;
          }
          state.view = "graph";
          if (viewStateByView.graph) {
            viewStateByView.graph.checked = true;
          }
          if (forceRebuild) {
            if (graphRuntime) {
              rebuildGraphRuntime();
            } else {
              renderGraph();
            }
            return;
          }
          if (!graphRuntime) {
            renderGraph();
            return;
          }
          updateGraphScene();
          kickGraphSimulation();
          renderGraphDetail(pagesById.get(state.selectedNodeId));
          requestAnimationFrame(() => {
            if (state.view === "graph") {
              updateGraphScene();
            }
          });
        }

        function resetGraphViewport() {
          if (!graphRuntime) {
            return;
          }
          graphRuntime.transform = { x: 0, y: 0, k: 1 };
          updateGraphTransform();
          kickGraphSimulation();
        }

        function applyGraphSettings(nextSettings) {
          const previousSettings = { ...state.graphSettings };
          const needsRebuild = graphSettingsNeedRebuild(previousSettings, nextSettings);
          state.graphSettings = {
            nodeScale: clamp(nextSettings.nodeScale, 0.55, 1.4),
            edgeScale: clamp(nextSettings.edgeScale, 0.55, 1.7),
            labelDensity: clamp(nextSettings.labelDensity, 0.35, 1.5),
            repulsionScale: clamp(nextSettings.repulsionScale, 0.45, 1.8),
            linkDistanceScale: clamp(nextSettings.linkDistanceScale, 0.6, 1.65),
            showLabels: Boolean(nextSettings.showLabels),
          };
          saveGraphSettings();
          syncGraphControlInputs();
          if (graphRuntime && !needsRebuild) {
            updateGraphScene();
            if (state.view === "graph") {
              renderGraphDetail(pagesById.get(state.selectedNodeId));
            }
          }
          refreshGraphFromControls(needsRebuild);
        }

        function stepGraphSimulation(timestamp = 0) {
          if (!graphRuntime || state.view !== "graph") {
            return;
          }

          const runtime = graphRuntime;
          const minFrameMs = 1000 / GRAPH_TARGET_FPS;
          if (timestamp && runtime.lastFrameTime && (timestamp - runtime.lastFrameTime) < minFrameMs) {
            runtime.rafId = requestAnimationFrame(stepGraphSimulation);
            return;
          }
          runtime.lastFrameTime = timestamp || performance.now();
          const nodes = runtime.nodes;
          const edges = runtime.edges;
          let totalMotion = 0;

          nodes.forEach((node) => {
            const anchor = runtime.anchors.get(node.graph_group) || { x: GRAPH_WIDTH / 2, y: GRAPH_HEIGHT / 2 };
            if (runtime.draggingNode && runtime.draggingNode.node.id === node.id) {
              return;
            }
            node.vx += (anchor.x - node.x) * 0.0032;
            node.vy += (anchor.y - node.y) * 0.0032;
            node.vx += ((GRAPH_WIDTH / 2) - node.x) * 0.00055;
            node.vy += ((GRAPH_HEIGHT / 2) - node.y) * 0.00055;
          });

          for (let i = 0; i < nodes.length; i += 1) {
            for (let j = i + 1; j < nodes.length; j += 1) {
              const left = nodes[i];
              const right = nodes[j];
              let dx = right.x - left.x;
              let dy = right.y - left.y;
              const distanceSquared = Math.max(dx * dx + dy * dy, 36);
              const distance = Math.sqrt(distanceSquared);
              dx /= distance;
              dy /= distance;
              const repulsion = (1180 * state.graphSettings.repulsionScale) / distanceSquared;
              left.vx -= dx * repulsion;
              left.vy -= dy * repulsion;
              right.vx += dx * repulsion;
              right.vy += dy * repulsion;
            }
          }

          edges.forEach((edge) => {
            const dx = edge.targetNode.x - edge.sourceNode.x;
            const dy = edge.targetNode.y - edge.sourceNode.y;
            const distance = Math.max(Math.hypot(dx, dy), 0.001);
            const stretch = distance - currentGraphIdealLength(edge);
            const force = stretch * edge.stiffness;
            const fx = (dx / distance) * force;
            const fy = (dy / distance) * force;
            edge.sourceNode.vx += fx;
            edge.sourceNode.vy += fy;
            edge.targetNode.vx -= fx;
            edge.targetNode.vy -= fy;
          });

          nodes.forEach((node) => {
            if (node.fx !== null && node.fy !== null) {
              node.x = node.fx;
              node.y = node.fy;
              node.vx = 0;
              node.vy = 0;
              return;
            }

            node.vx *= 0.84;
            node.vy *= 0.84;
            node.vx = clamp(node.vx, -10, 10);
            node.vy = clamp(node.vy, -10, 10);
            node.x = clamp(node.x + node.vx, 42, GRAPH_WIDTH - 42);
            node.y = clamp(node.y + node.vy, 42, GRAPH_HEIGHT - 42);
            totalMotion += Math.abs(node.vx) + Math.abs(node.vy);
          });

          updateGraphScene();

          if (runtime.draggingNode || runtime.panning || totalMotion > 0.52 || runtime.settledFrames < 4) {
            runtime.settledFrames = totalMotion > 0.52 ? 0 : runtime.settledFrames + 1;
            runtime.rafId = requestAnimationFrame(stepGraphSimulation);
          } else {
            runtime.rafId = 0;
            updateGraphScene();
          }
        }

        function kickGraphSimulation() {
          if (!graphRuntime || graphRuntime.rafId) {
            return;
          }
          graphRuntime.settledFrames = 0;
          graphRuntime.lastFrameTime = 0;
          graphRuntime.rafId = requestAnimationFrame(stepGraphSimulation);
        }

        function renderGraphDetail(page) {
          if (!page) {
            graphDetail.innerHTML = `
              <p class="eyebrow">${escapeHtml(t("graph_detail"))}</p>
              <h2>${escapeHtml(t("select_node"))}</h2>
              <p class="subtle">${escapeHtml(t("graph_detail_help"))}</p>
            `;
            return;
          }

          const tagHtml = page.graph_tags.length
            ? page.graph_tags
            .slice(0, 8)
            .map((tag) => `<span class="mini-chip">${escapeHtml(translateLabel(tag))}</span>`)
            .join("")
            : `<span class="mini-chip">${escapeHtml(t("no_relationship_tags"))}</span>`;

          const pdfLink = page.pdf_href
            ? `<a class="card-link secondary" ${renderHrefAttributes(page.pdf_href, page.pdf_file_href, page.pdf_http_href)}>${escapeHtml(t("open_pdf"))}</a>`
            : "";
          const articleLink = page.article_href
            ? `<a class="card-link tertiary" ${renderExternalHrefAttributes(page.article_href)}>${escapeHtml(t("open_article"))}</a>`
            : "";

          const availableEdges = graphRuntime ? graphRuntime.edges : data.paper_edges;
          const linkedTitles = availableEdges
            .filter((edge) => edge.source === page.id || edge.target === page.id)
            .map((edge) => {
              const related = pagesById.get(edge.source === page.id ? edge.target : edge.source);
              if (!related) {
                return null;
              }
              return { page: related, reasons: edge.reasons || [], strength: edge.strength || 1 };
            })
            .filter(Boolean)
            .sort((left, right) => right.strength - left.strength || left.page.title.localeCompare(right.page.title));

          const linkedHtml = linkedTitles.length
            ? `<ul class="detail-links">${linkedTitles
                .slice(0, 12)
                .map((item) => `
                  <li>
                    <a class="detail-link-title" ${renderHrefAttributes(item.page.href, item.page.file_href, item.page.http_href)}>${escapeHtml(item.page.title)}</a>
                    <div class="detail-link-reasons">${(item.reasons || [])
                      .slice(0, 4)
                      .map((reason) => `<span class="relation-chip">${escapeHtml(translateLabel(reason))}</span>`)
                      .join("")}</div>
                  </li>
                `)
                .join("")}</ul>`
            : `<p class="subtle">${escapeHtml(t("no_related_papers"))}</p>`;

          graphDetail.innerHTML = `
            <p class="eyebrow">${escapeHtml(translateLabel(page.graph_group || page.section_label))}</p>
            <h2>${escapeHtml(page.title)}</h2>
            <p class="graph-excerpt">${escapeHtml(page.excerpt)}</p>
            <div class="graph-detail-metrics">
              <div class="graph-metric-chip">
                <span>${escapeHtml(t("graph_metric_theme"))}</span>
                <strong>${escapeHtml(translateLabel(page.graph_group || page.section_label))}</strong>
              </div>
              <div class="graph-metric-chip">
                <span>${escapeHtml(t("graph_metric_relations"))}</span>
                <strong>${linkedTitles.length}</strong>
              </div>
              <div class="graph-metric-chip">
                <span>${escapeHtml(t("graph_metric_year"))}</span>
                <strong>${escapeHtml(page.year ? String(page.year) : "—")}</strong>
              </div>
            </div>
            <div class="card-tags">${tagHtml}</div>
            <div class="card-actions">
              <a class="card-link" ${renderHrefAttributes(page.href, page.file_href, page.http_href)}>${escapeHtml(t("open_page"))}</a>
              ${articleLink}
              ${pdfLink}
            </div>
            <h3>${escapeHtml(t("related_papers"))}</h3>
            ${linkedHtml}
          `;
        }

        function renderGraph() {
          const visiblePages = filteredPapers();
          const visibleIds = new Set(visiblePages.map((page) => page.id));
          const visibleEdges = data.paper_edges.filter((edge) => visibleIds.has(edge.source) && visibleIds.has(edge.target));

          if (!visiblePages.length) {
            stopGraphAnimation(true);
            renderGraphDetail(null);
            graphSvg.innerHTML = `
              <text x="${GRAPH_WIDTH / 2}" y="${GRAPH_HEIGHT / 2}" text-anchor="middle" class="graph-empty">${escapeHtml(t("no_papers_graph"))}</text>
            `;
            clearGraphCanvas();
            return;
          }

          if (!state.selectedNodeId || !visibleIds.has(state.selectedNodeId)) {
            state.selectedNodeId = visiblePages[0].id;
          }

          const nextKey = graphLayoutKey(visiblePages, visibleEdges);
          if (!graphRuntime || graphRuntime.key !== nextKey) {
            stopGraphAnimation(true);
            graphRuntime = createGraphRuntime(visiblePages, visibleEdges);
            initializeGraphScene();
            kickGraphSimulation();
          } else {
            updateGraphScene();
          }

          renderGraphDetail(pagesById.get(state.selectedNodeId));
        }

        function setView(view) {
          state.view = view;
          if (viewStateByView[view]) {
            viewStateByView[view].checked = true;
          }
          viewButtons.forEach((button) => button.classList.toggle("active", button.dataset.view === view));
          document.querySelectorAll(".dashboard-view").forEach((section) => {
            const isActive = section.id === `${view}-view`;
            section.classList.toggle("hidden", !isActive);
            section.classList.toggle("active", isActive);
          });
          if (view === "graph") {
            renderGraph();
            return;
          }
          stopGraphAnimation(false);
        }

        function renderAll() {
          renderTagChips();
          renderActiveFilters();
          renderCounts();
          renderPapers();
          renderDatabase();
          renderPages();
          if (state.view === "graph") {
            renderGraph();
          }
        }

        searchInput.addEventListener("input", () => {
          state.search = searchInput.value;
          renderAll();
        });

        clearFiltersButton.addEventListener("click", () => {
          state.search = "";
          state.tags.clear();
          searchInput.value = "";
          renderAll();
        });

        function bindGraphRangeInput(input, handler) {
          input.addEventListener("input", handler);
          input.addEventListener("change", handler);
        }

        bindGraphRangeInput(graphNodeScaleInput, () => {
          applyGraphSettings({
            ...state.graphSettings,
            nodeScale: Number(graphNodeScaleInput.value) / 100,
          });
        });

        bindGraphRangeInput(graphEdgeScaleInput, () => {
          applyGraphSettings({
            ...state.graphSettings,
            edgeScale: Number(graphEdgeScaleInput.value) / 100,
          });
        });

        bindGraphRangeInput(graphLabelDensityInput, () => {
          applyGraphSettings({
            ...state.graphSettings,
            labelDensity: Number(graphLabelDensityInput.value) / 100,
          });
        });

        bindGraphRangeInput(graphRepulsionScaleInput, () => {
          applyGraphSettings({
            ...state.graphSettings,
            repulsionScale: Number(graphRepulsionScaleInput.value) / 100,
          });
        });

        bindGraphRangeInput(graphLinkDistanceScaleInput, () => {
          applyGraphSettings({
            ...state.graphSettings,
            linkDistanceScale: Number(graphLinkDistanceScaleInput.value) / 100,
          });
        });

        graphShowLabelsInput.addEventListener("change", () => {
          applyGraphSettings({
            ...state.graphSettings,
            showLabels: graphShowLabelsInput.checked,
          });
        });

        graphResetButton.addEventListener("click", () => {
          applyGraphSettings({ ...DEFAULT_GRAPH_SETTINGS });
          resetGraphViewport();
        });

        window.addEventListener("resize", () => {
          if (!graphRuntime) {
            return;
          }
          configureGraphCanvas();
          drawGraphScene();
        });

        databaseSortSelect.addEventListener("change", () => {
          state.databaseSettings.sortKey = databaseSortSelect.value;
          saveDatabaseSettings();
          syncDatabaseControlInputs();
          renderDatabase();
        });

        databaseSortDirectionButton.addEventListener("click", () => {
          state.databaseSettings.sortDirection = state.databaseSettings.sortDirection === "asc" ? "desc" : "asc";
          saveDatabaseSettings();
          syncDatabaseControlInputs();
          renderDatabase();
        });

        databaseGroupSelect.addEventListener("change", () => {
          state.databaseSettings.groupKey = databaseGroupSelect.value;
          saveDatabaseSettings();
          syncDatabaseControlInputs();
          renderDatabase();
        });

        databaseDensitySelect.addEventListener("change", () => {
          state.databaseSettings.density = databaseDensitySelect.value;
          saveDatabaseSettings();
          syncDatabaseControlInputs();
          renderDatabase();
        });

        databaseExportButton.addEventListener("click", () => {
          exportDatabaseCsv();
        });

        viewButtons.forEach((button) => {
          button.addEventListener("click", () => {
            setView(button.dataset.view);
            renderAll();
          });
          button.addEventListener("keydown", (event) => {
            if (event.key !== "Enter" && event.key !== " ") {
              return;
            }
            event.preventDefault();
            button.click();
          });
        });

        viewStateInputs.forEach((input) => {
          input.addEventListener("change", () => {
            if (!input.checked) {
              return;
            }
            setView(input.dataset.view);
          });
        });

        langButtons.forEach((button) => {
          button.addEventListener("click", () => {
            state.language = button.dataset.lang;
            localStorage.setItem("paper_atlas_lang", state.language);
            applyLanguage();
            renderAll();
          });
        });

        applyLanguage();
        renderAll();
        setView("papers");
      })();
    </script>
  </body>
</html>
"""
)


STYLE_TEXT = """
:root {
  --paper: #f7f2e7;
  --panel: rgba(255, 252, 245, 0.88);
  --panel-strong: rgba(255, 250, 241, 0.95);
  --ink: #221d18;
  --muted: #6a6259;
  --accent: #7a3520;
  --accent-soft: #edd8c4;
  --line: rgba(77, 60, 44, 0.16);
  --shadow: 0 22px 60px rgba(45, 30, 17, 0.12);
  --font-sans: Arial, "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
}

* {
  box-sizing: border-box;
}

html {
  min-height: 100%;
  background:
    radial-gradient(circle at top left, rgba(195, 128, 86, 0.18), transparent 28%),
    radial-gradient(circle at top right, rgba(117, 72, 52, 0.12), transparent 22%),
    linear-gradient(180deg, #f5ead9 0%, #efe3d0 100%);
}

body {
  margin: 0;
  color: var(--ink);
  font-family: var(--font-sans);
  line-height: 1.65;
}

a {
  color: var(--accent);
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

code {
  font-family: "SFMono-Regular", "Menlo", "Consolas", monospace;
  background: rgba(122, 53, 32, 0.08);
  border-radius: 0.35rem;
  padding: 0.15rem 0.35rem;
  font-size: 0.92em;
}

pre {
  background: #201a17;
  color: #f7efe4;
  border-radius: 1rem;
  padding: 1rem 1.1rem;
  overflow-x: auto;
  box-shadow: inset 0 0 0 1px rgba(255, 255, 255, 0.08);
}

pre code {
  background: transparent;
  padding: 0;
  color: inherit;
}

.shell {
  display: grid;
  grid-template-columns: minmax(250px, 300px) minmax(0, 1fr);
  gap: 1.5rem;
  max-width: 1600px;
  margin: 0 auto;
  padding: 1.5rem;
}

.sidebar,
.content {
  backdrop-filter: blur(8px);
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 1.4rem;
  box-shadow: var(--shadow);
}

.sidebar {
  padding: 1.25rem 1rem;
  position: sticky;
  top: 1rem;
  height: calc(100vh - 2rem);
  overflow-y: auto;
}

.content {
  padding: 1.6rem 1.8rem 2rem;
}

.brand {
  padding: 0.3rem 0.35rem 1rem;
  border-bottom: 1px solid var(--line);
  margin-bottom: 1rem;
}

.brand-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.55rem;
}

.brand-topbar .eyebrow {
  margin: 0;
}

.home-logo-link {
  display: inline-flex;
  align-items: center;
  gap: 0.58rem;
  padding: 0.42rem 0.68rem 0.42rem 0.48rem;
  border-radius: 999px;
  border: 1px solid rgba(122, 53, 32, 0.16);
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.94) 0%, rgba(248, 240, 229, 0.92) 100%);
  color: #5d2618;
  font-size: 0.84rem;
  font-weight: 700;
  line-height: 1;
  box-shadow: 0 12px 24px rgba(75, 45, 24, 0.08);
}

.home-logo-link:hover {
  text-decoration: none;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.98) 0%, rgba(249, 242, 232, 0.96) 100%);
}

.home-logo-mark {
  width: 1.65rem;
  height: 1.65rem;
  flex: 0 0 auto;
  border-radius: 0.5rem;
  overflow: hidden;
}

.home-logo-text {
  font-family: var(--font-sans);
  letter-spacing: 0.03em;
}

.brand h1,
.page-header h1,
.dashboard-hero h1 {
  margin: 0;
  line-height: 1.08;
  font-weight: 700;
}

.brand h1 {
  font-size: 1.75rem;
}

.subtle,
.meta-chip,
.eyebrow {
  color: var(--muted);
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.72rem;
  margin: 0 0 0.35rem;
  font-family: var(--font-sans);
}

.dashboard-link,
.ghost-button,
.view-button,
.tag-chip,
.lang-button,
.card-link,
.search-input,
.page-row-link,
.quick-links a {
  font-family: var(--font-sans);
}

.brand-link {
  color: inherit;
  text-decoration: none;
}

.dashboard-link {
  display: inline-flex;
  margin-top: 0.9rem;
  padding: 0.55rem 0.82rem;
  border-radius: 999px;
  background: var(--accent-soft);
  color: #4f1f12;
  font-size: 0.92rem;
  font-weight: 700;
}

.dashboard-link:hover {
  text-decoration: none;
  background: #e4c6ac;
}

.brand-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin-top: 0.9rem;
}

.brand-actions .dashboard-link {
  margin-top: 0;
}

.dashboard-link.secondary-link {
  background: rgba(255, 255, 255, 0.76);
  border: 1px solid rgba(122, 53, 32, 0.16);
}

.dashboard-link.secondary-link:hover {
  background: rgba(255, 255, 255, 0.94);
}

.language-toggle {
  margin-top: 0.95rem;
}

.language-buttons {
  display: flex;
  gap: 0.45rem;
  margin-top: 0.45rem;
}

.lang-button {
  border: 1px solid rgba(77, 60, 44, 0.16);
  background: rgba(255, 255, 255, 0.72);
  color: var(--ink);
  border-radius: 999px;
  padding: 0.42rem 0.78rem;
  font-size: 0.88rem;
  font-weight: 700;
  cursor: pointer;
}

.lang-button.active {
  background: linear-gradient(135deg, #8e3c27 0%, #b96845 100%);
  color: white;
  border-color: transparent;
}

.nav-group {
  margin-bottom: 1.1rem;
}

.nav-group h2,
.control-label {
  margin: 0 0 0.45rem;
  font-size: 0.82rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--muted);
  font-family: var(--font-sans);
}

.nav-group ul,
.quick-links {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-group li,
.quick-links li {
  margin: 0;
}

.nav-group a,
.quick-links a {
  display: block;
  padding: 0.42rem 0.5rem;
  border-radius: 0.75rem;
  color: var(--ink);
}

.nav-group li.current a {
  background: var(--accent-soft);
  color: #4f1f12;
  font-weight: 700;
}

.nav-group a:hover,
.quick-links a:hover {
  background: rgba(122, 53, 32, 0.07);
  text-decoration: none;
}

.page-header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  margin-bottom: 1.2rem;
}

.page-header h1,
.dashboard-hero h1 {
  font-size: clamp(2rem, 3vw, 3rem);
}

.meta-chip {
  padding: 0.55rem 0.85rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.65);
  white-space: nowrap;
  font-family: var(--font-sans);
  font-size: 0.9rem;
}

.meta-panel {
  margin: 0 0 1.5rem;
  padding: 1rem 1.1rem;
  background: rgba(255, 255, 255, 0.66);
  border: 1px solid var(--line);
  border-radius: 1rem;
}

.meta-panel h2 {
  margin: 0 0 0.7rem;
  font-size: 1rem;
}

.meta-panel dl {
  margin: 0;
}

.meta-panel div {
  display: grid;
  grid-template-columns: 150px minmax(0, 1fr);
  gap: 0.5rem 1rem;
  padding: 0.22rem 0;
}

.meta-panel dt {
  font-weight: 700;
  color: var(--muted);
}

.meta-panel dd {
  margin: 0;
}

.page-body > *:first-child {
  margin-top: 0;
}

.page-body h1,
.page-body h2,
.page-body h3,
.page-body h4,
.page-body h5,
.page-body h6 {
  margin-top: 1.6rem;
  margin-bottom: 0.6rem;
  line-height: 1.18;
}

.page-body h2 {
  font-size: 1.55rem;
  border-bottom: 1px solid var(--line);
  padding-bottom: 0.35rem;
}

.page-body h3 {
  font-size: 1.2rem;
}

.page-body p,
.page-body ul,
.page-body ol,
.page-body pre,
.page-body blockquote {
  margin-top: 0.8rem;
  margin-bottom: 0.8rem;
}

.page-body ul,
.page-body ol {
  padding-left: 1.35rem;
}

.page-body li + li {
  margin-top: 0.28rem;
}

.page-body blockquote {
  margin-left: 0;
  padding: 0.8rem 1rem;
  border-left: 4px solid var(--accent);
  background: rgba(122, 53, 32, 0.06);
  border-radius: 0 0.8rem 0.8rem 0;
}

.dashboard-shell {
  align-items: start;
}

.dashboard-sidebar {
  background:
    linear-gradient(180deg, rgba(255, 250, 241, 0.97) 0%, rgba(247, 242, 231, 0.88) 100%);
}

.dashboard-content {
  min-height: calc(100vh - 3rem);
}

.dashboard-hero {
  display: grid;
  grid-template-columns: minmax(0, 1.2fr) minmax(320px, 0.8fr);
  gap: 1.25rem;
  align-items: start;
  margin-bottom: 1.2rem;
}

.hero-copy {
  margin: 0.8rem 0 0;
  max-width: 58ch;
  color: #4e4740;
  font-size: 1.02rem;
}

.hero-stats {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.9rem;
}

.stat-card,
.side-block,
.status-bar,
.paper-card,
.page-row,
.graph-detail {
  background: var(--panel-strong);
  border: 1px solid var(--line);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.65);
}

.stat-card {
  border-radius: 1.1rem;
  padding: 1rem 1.05rem;
}

.stat-label {
  display: block;
  color: var(--muted);
  font-size: 0.82rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-family: var(--font-sans);
}

.stat-card strong {
  display: block;
  margin-top: 0.35rem;
  font-size: 2rem;
  line-height: 1;
}

.side-block {
  padding: 1rem;
  border-radius: 1rem;
  margin-bottom: 1rem;
}

.side-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  margin-bottom: 0.5rem;
}

.search-input {
  width: 100%;
  appearance: none;
  border: 1px solid rgba(77, 60, 44, 0.24);
  background: rgba(255, 255, 255, 0.88);
  color: var(--ink);
  border-radius: 0.9rem;
  padding: 0.82rem 0.9rem;
  font-size: 1rem;
}

.search-input:focus {
  outline: 2px solid rgba(122, 53, 32, 0.28);
  border-color: rgba(122, 53, 32, 0.38);
}

.small-note {
  font-size: 0.92rem;
  margin-bottom: 0;
}

.view-switch {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.55rem;
}

.view-state-toggle {
  position: absolute;
  opacity: 0;
  pointer-events: none;
}

.view-button,
.ghost-button,
.tag-chip,
.lang-button,
.card-link {
  appearance: none;
  border: 1px solid rgba(77, 60, 44, 0.18);
  border-radius: 0.85rem;
  cursor: pointer;
  transition: transform 140ms ease, background 140ms ease, border-color 140ms ease;
}

.view-button,
.ghost-button,
.tag-chip,
.lang-button {
  background: rgba(255, 255, 255, 0.85);
  color: var(--ink);
}

.view-button {
  display: block;
  text-align: left;
  padding: 0.7rem 0.85rem;
  font-size: 0.96rem;
  font-weight: 600;
}

.view-button.active {
  background: linear-gradient(135deg, #8e3c27 0%, #b96845 100%);
  color: white;
  border-color: rgba(142, 60, 39, 0.78);
}

.ghost-button {
  padding: 0.4rem 0.72rem;
  font-size: 0.88rem;
}

.ghost-button:hover,
.view-button:hover,
.tag-chip:hover,
.lang-button:hover,
.card-link:hover {
  transform: translateY(-1px);
  text-decoration: none;
}

.chip-list,
.card-tags,
.active-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.tag-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.45rem 0.7rem;
  font-size: 0.9rem;
}

.tag-chip small {
  color: var(--muted);
}

.tag-chip.active {
  background: var(--accent-soft);
  border-color: rgba(122, 53, 32, 0.34);
  color: #4f1f12;
}

.legend-list {
  display: grid;
  gap: 0.55rem;
}

.legend-row {
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 0.65rem;
  align-items: center;
  font-family: var(--font-sans);
  font-size: 0.92rem;
}

.legend-dot {
  width: 0.78rem;
  height: 0.78rem;
  border-radius: 999px;
}

.legend-count {
  color: var(--muted);
}

.status-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  padding: 0.9rem 1rem;
  border-radius: 1rem;
  margin-bottom: 1rem;
}

.status-copy {
  display: flex;
  flex-direction: column;
}

.active-chip,
.mini-chip,
.section-pill,
.year-pill {
  display: inline-flex;
  align-items: center;
  border-radius: 999px;
  font-family: var(--font-sans);
}

.active-chip,
.mini-chip {
  background: rgba(122, 53, 32, 0.08);
  padding: 0.28rem 0.55rem;
  font-size: 0.82rem;
  color: #5a463b;
}

.section-pill {
  padding: 0.28rem 0.58rem;
  font-size: 0.76rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: white;
}

.section-core { background: #946448; }
.section-sources { background: #8e3c27; }
.section-concepts { background: #275d5d; }
.section-queries { background: #755f24; }
.section-syntheses { background: #4f3a77; }

.year-pill {
  background: rgba(77, 60, 44, 0.08);
  color: var(--muted);
  padding: 0.28rem 0.55rem;
  font-size: 0.82rem;
}

.dashboard-view,
.dashboard-view.hidden,
.hidden {
  display: none;
}

#view-tab-papers:checked ~ .dashboard-content #papers-view,
#view-tab-database:checked ~ .dashboard-content #database-view,
#view-tab-pages:checked ~ .dashboard-content #pages-view,
#view-tab-graph:checked ~ .dashboard-content #graph-view {
  display: block;
}

#view-tab-papers:checked ~ .dashboard-sidebar .view-button[data-view="papers"],
#view-tab-database:checked ~ .dashboard-sidebar .view-button[data-view="database"],
#view-tab-pages:checked ~ .dashboard-sidebar .view-button[data-view="pages"],
#view-tab-graph:checked ~ .dashboard-sidebar .view-button[data-view="graph"] {
  background: linear-gradient(135deg, #8e3c27 0%, #b96845 100%);
  color: white;
  border-color: rgba(142, 60, 39, 0.78);
}

.paper-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.paper-card,
.page-row,
.graph-detail {
  border-radius: 1.15rem;
}

.paper-card {
  display: flex;
  flex-direction: column;
  gap: 0.9rem;
  padding: 1rem 1rem 1.05rem;
  min-height: 290px;
}

.paper-card h2 {
  margin: 0;
  font-size: 1.16rem;
  line-height: 1.25;
}

.card-topline,
.page-row-head,
.card-actions,
.page-row-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.65rem;
  flex-wrap: wrap;
}

.card-excerpt,
.page-row-excerpt,
.graph-excerpt {
  margin: 0;
  color: #4e4740;
}

.card-actions {
  margin-top: auto;
}

.card-link {
  display: inline-flex;
  justify-content: center;
  padding: 0.55rem 0.82rem;
  background: linear-gradient(135deg, #8e3c27 0%, #b96845 100%);
  color: white;
  font-size: 0.92rem;
  font-weight: 700;
}

.card-link.secondary {
  background: rgba(255, 255, 255, 0.88);
  color: var(--ink);
}

.card-link.tertiary {
  background: rgba(122, 53, 32, 0.08);
  color: #6e2e1d;
}

.page-list {
  display: grid;
  gap: 0.85rem;
}

.database-toolbar,
.database-group {
  display: grid;
  gap: 0.85rem;
}

.database-toolbar {
  margin-bottom: 0.9rem;
}

.database-toolbar-head,
.database-group-header,
.database-inline-controls,
.database-actions,
.database-summary {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  flex-wrap: wrap;
}

.database-toolbar-head,
.database-group-header {
  justify-content: space-between;
}

.database-controls {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 0.75rem;
}

.database-control {
  display: grid;
  gap: 0.45rem;
  padding: 0.85rem 0.95rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--panel-strong);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.65);
}

.database-control span {
  font-size: 0.84rem;
  color: var(--muted);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-family: var(--font-sans);
}

.database-control select,
.database-inline-controls .ghost-button {
  font-family: var(--font-sans);
}

.database-control select {
  appearance: none;
  border: 1px solid rgba(77, 60, 44, 0.18);
  border-radius: 0.85rem;
  background: rgba(255, 255, 255, 0.9);
  color: var(--ink);
  padding: 0.62rem 0.78rem;
  font-size: 0.94rem;
}

.database-inline-controls {
  flex-wrap: nowrap;
}

.database-inline-controls select {
  flex: 1 1 auto;
}

.database-icon-button {
  min-width: 2.8rem;
  padding: 0.62rem 0.78rem;
}

.database-summary {
  gap: 0.75rem;
}

.summary-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 0.75rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.82);
  color: var(--ink);
}

.summary-chip strong {
  font-size: 1rem;
}

.summary-chip span {
  color: var(--muted);
  font-size: 0.85rem;
}

.subtle-chip {
  background: rgba(255, 255, 255, 0.72);
}

.database-groups {
  display: grid;
  gap: 1rem;
}

.database-group-header h3 {
  margin: 0;
  font-size: 1.1rem;
}

.database-table-wrap {
  display: block;
  max-width: 100%;
  overflow-x: auto;
  overflow-y: hidden;
  -webkit-overflow-scrolling: touch;
  scrollbar-gutter: stable both-edges;
  touch-action: pan-x;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: var(--panel-strong);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.65);
}

.database-table {
  width: 100%;
  min-width: 1020px;
  border-collapse: collapse;
  font-family: var(--font-sans);
}

#database-view {
  overflow-x: auto;
}

.database-table th,
.database-table td {
  padding: 0.9rem 0.85rem;
  border-bottom: 1px solid rgba(77, 60, 44, 0.1);
  vertical-align: top;
  text-align: left;
}

.database-table-wrap.compact .database-table th,
.database-table-wrap.compact .database-table td {
  padding: 0.62rem 0.7rem;
}

.database-table th {
  position: sticky;
  top: 0;
  background: rgba(247, 242, 231, 0.96);
  color: var(--muted);
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  z-index: 1;
}

.database-table tbody tr:hover {
  background: rgba(122, 53, 32, 0.04);
}

.database-title-cell {
  min-width: 320px;
}

.database-title-link {
  color: var(--ink);
  font-weight: 700;
  font-size: 1rem;
}

.database-subtle {
  margin: 0.3rem 0 0;
  color: var(--muted);
  font-size: 0.9rem;
  line-height: 1.45;
}

.database-tag-cell {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  min-width: 180px;
}

.table-action {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 0.48rem 0.72rem;
  border-radius: 0.78rem;
  background: linear-gradient(135deg, #8e3c27 0%, #b96845 100%);
  color: white;
  font-size: 0.88rem;
  font-weight: 700;
}

.table-action.secondary {
  background: rgba(255, 255, 255, 0.88);
  color: var(--ink);
}

.table-action.tertiary {
  background: rgba(122, 53, 32, 0.08);
  color: #6e2e1d;
}

.page-row {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  gap: 1rem;
  align-items: center;
  padding: 0.95rem 1rem;
}

.page-row-link {
  font-size: 1.02rem;
  font-weight: 700;
  color: var(--ink);
}

.empty-state {
  margin: 1rem 0 0;
  padding: 1rem 1.1rem;
  border: 1px dashed rgba(77, 60, 44, 0.22);
  border-radius: 1rem;
  color: var(--muted);
  background: rgba(255, 255, 255, 0.55);
}

.graph-toolbar {
  display: grid;
  gap: 1rem;
  margin-bottom: 1rem;
}

.graph-toolbar-copy {
  max-width: 82ch;
  font-size: 0.96rem;
}

.graph-controls-panel {
  display: grid;
  gap: 0.7rem;
  padding: 1rem 1.05rem;
  border-radius: 1.15rem;
  border: 1px solid rgba(77, 60, 44, 0.12);
  background:
    linear-gradient(180deg, rgba(255, 253, 249, 0.92) 0%, rgba(249, 240, 229, 0.88) 100%);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.7);
}

.graph-controls-heading {
  margin-bottom: 0;
}

.graph-controls {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 0.7rem;
}

.graph-control {
  display: grid;
  gap: 0.45rem;
  padding: 0.8rem 0.9rem;
  border: 1px solid var(--line);
  border-radius: 1rem;
  background: rgba(255, 255, 255, 0.82);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.65);
}

.graph-control-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  font-size: 0.88rem;
  font-weight: 700;
  color: var(--ink);
}

.graph-control-value {
  color: var(--muted);
  font-size: 0.82rem;
  font-variant-numeric: tabular-nums;
}

.graph-range {
  width: 100%;
  margin: 0;
  accent-color: #8e3c27;
}

.graph-control-action {
  align-content: center;
}

.graph-control-action .ghost-button {
  width: 100%;
  padding: 0.72rem 0.85rem;
  font-size: 0.92rem;
}

.graph-toggle {
  align-content: center;
}

.graph-toggle-input {
  width: 100%;
  height: 1.2rem;
  margin: 0.1rem 0 0;
  accent-color: #8e3c27;
}

.graph-layout {
  display: grid;
  grid-template-columns: minmax(0, 1.28fr) minmax(320px, 0.62fr);
  gap: 1.15rem;
  align-items: start;
}

.graph-stage {
  position: relative;
  height: clamp(420px, 68vh, 720px);
  background:
    radial-gradient(circle at 18% 18%, rgba(250, 209, 174, 0.42), transparent 26%),
    radial-gradient(circle at 82% 20%, rgba(214, 155, 120, 0.24), transparent 22%),
    radial-gradient(circle at 50% 82%, rgba(255, 255, 255, 0.68), transparent 28%),
    linear-gradient(180deg, rgba(255, 251, 246, 0.98) 0%, rgba(245, 236, 224, 0.94) 100%);
  border: 1px solid rgba(77, 60, 44, 0.15);
  border-radius: 1.35rem;
  overflow: hidden;
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.72),
    0 18px 40px rgba(58, 37, 20, 0.08);
}

.graph-stage::before,
.graph-stage::after {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
}

.graph-stage::before {
  background-image:
    linear-gradient(rgba(122, 53, 32, 0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(122, 53, 32, 0.04) 1px, transparent 1px);
  background-size: 32px 32px;
  mask-image: linear-gradient(180deg, rgba(0, 0, 0, 0.5), transparent 92%);
}

.graph-stage::after {
  inset: auto 1.1rem 1rem 1.1rem;
  height: 22%;
  border-radius: 999px;
  background: radial-gradient(circle at center, rgba(255, 255, 255, 0.72), transparent 72%);
  filter: blur(30px);
  opacity: 0.7;
}

.graph-stage-header {
  position: absolute;
  top: 0.95rem;
  left: 1rem;
  right: 1rem;
  z-index: 3;
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  pointer-events: none;
}

.graph-stage-copy {
  display: grid;
  gap: 0.55rem;
  max-width: min(100%, 840px);
}

.graph-stage-pill {
  display: inline-flex;
  align-items: center;
  width: fit-content;
  padding: 0.34rem 0.65rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.84);
  border: 1px solid rgba(77, 60, 44, 0.14);
  color: #73412c;
  font-size: 0.76rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  box-shadow: 0 10px 20px rgba(55, 33, 18, 0.08);
}

.graph-legend {
  display: flex;
  flex-wrap: wrap;
  gap: 0.45rem;
}

.graph-legend-chip {
  display: inline-flex;
  align-items: center;
  gap: 0.48rem;
  padding: 0.42rem 0.66rem;
  border-radius: 999px;
  border: 1px solid rgba(77, 60, 44, 0.14);
  background: rgba(255, 255, 255, 0.78);
  color: #4e433b;
  font-size: 0.82rem;
  box-shadow: 0 10px 18px rgba(55, 33, 18, 0.05);
}

.graph-legend-dot {
  width: 0.7rem;
  height: 0.7rem;
  border-radius: 999px;
  flex: 0 0 auto;
}

.graph-legend-chip small {
  color: var(--muted);
  font-size: 0.76rem;
}

.graph-canvas,
.graph-svg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.graph-canvas {
  pointer-events: none;
}

.graph-svg {
  touch-action: none;
  cursor: grab;
  background: transparent;
}

.graph-svg.panning,
.graph-svg.dragging {
  cursor: grabbing;
}

.graph-edge {
  stroke: rgba(77, 60, 44, 0.26);
  stroke-linecap: round;
  transition: opacity 160ms ease, stroke 160ms ease;
}

.graph-edge.dimmed {
  opacity: 0.12 !important;
}

.graph-edge.related {
  stroke: rgba(122, 53, 32, 0.5);
}

.graph-node {
  cursor: pointer;
}

.graph-node.static-node {
  cursor: pointer;
}

.graph-node circle {
  transition: stroke-width 120ms ease, opacity 120ms ease;
  stroke: rgba(255, 255, 255, 0.92);
  stroke-width: 2.2;
}

.graph-node.dimmed {
  opacity: 0.28;
}

.graph-node:hover circle,
.graph-node.selected circle {
  transform: scale(1.12);
  stroke-width: 3.4;
}

.graph-label {
  fill: #3b3028;
  font-size: 10.5px;
  text-anchor: middle;
  font-family: var(--font-sans);
  paint-order: stroke fill;
  stroke: rgba(255, 252, 245, 0.98);
  stroke-width: 4.5px;
  stroke-linejoin: round;
  opacity: 0.94;
}

.graph-label.hidden {
  opacity: 0;
}

.graph-svg.panning .graph-label,
.graph-svg.dragging .graph-label {
  opacity: 0 !important;
}

.graph-empty {
  fill: #6a6259;
  font-size: 18px;
  font-family: var(--font-sans);
}

.graph-detail {
  padding: 1.15rem 1.15rem 1.2rem;
  border-radius: 1.35rem;
  background:
    linear-gradient(180deg, rgba(255, 254, 250, 0.96) 0%, rgba(248, 240, 228, 0.92) 100%);
  box-shadow:
    inset 0 1px 0 rgba(255, 255, 255, 0.75),
    0 18px 40px rgba(58, 37, 20, 0.08);
}

.graph-detail h2,
.graph-detail h3 {
  margin-top: 0;
}

.graph-detail h3 {
  font-size: 1rem;
}

.graph-detail-metrics {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.6rem;
  margin: 0.95rem 0 0.8rem;
}

.graph-metric-chip {
  display: grid;
  gap: 0.18rem;
  padding: 0.72rem 0.78rem;
  border-radius: 1rem;
  border: 1px solid rgba(77, 60, 44, 0.12);
  background: rgba(255, 255, 255, 0.78);
}

.graph-metric-chip span {
  color: var(--muted);
  font-size: 0.74rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.graph-metric-chip strong {
  font-size: 0.98rem;
  line-height: 1.2;
  color: #30261f;
}

.detail-links {
  margin: 0.75rem 0 0;
  padding-left: 0;
  list-style: none;
  display: grid;
  gap: 0.72rem;
}

.detail-links li {
  padding: 0.82rem 0.88rem;
  border-radius: 1rem;
  border: 1px solid rgba(77, 60, 44, 0.1);
  background: rgba(255, 255, 255, 0.76);
}

.detail-link-title {
  font-weight: 700;
  color: #342b24;
}

.detail-link-reasons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.35rem;
  margin-top: 0.35rem;
}

.relation-chip {
  display: inline-flex;
  align-items: center;
  padding: 0.2rem 0.5rem;
  border-radius: 999px;
  background: rgba(122, 53, 32, 0.08);
  color: var(--ink);
  font-size: 0.78rem;
  font-family: var(--font-sans);
}

.graph-strength {
  margin-top: 0.65rem;
  font-size: 0.9rem;
  color: var(--muted);
}

@media (max-width: 1180px) {
  .dashboard-hero,
  .graph-layout {
    grid-template-columns: 1fr;
  }

  .graph-detail-metrics {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

@media (max-width: 980px) {
  .shell {
    grid-template-columns: 1fr;
  }

  .sidebar {
    position: static;
    height: auto;
  }

  .page-header,
  .status-bar,
  .page-row {
    grid-template-columns: 1fr;
    flex-direction: column;
  }

  .graph-controls {
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  }

  .database-controls {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 720px) {
  .graph-stage {
    height: clamp(360px, 56vh, 560px);
  }

  .graph-stage-header {
    top: 0.85rem;
    left: 0.85rem;
    right: 0.85rem;
  }

  .graph-detail-metrics {
    grid-template-columns: 1fr;
  }

  .database-table {
    min-width: 880px;
  }
}
"""


KEYWORD_TAGS = [
    ([r"\brare diseases?\b"], "Rare Disease"),
    ([r"\bclinical\b", r"\bdiagnostic\b", r"\bpatients?\b"], "Clinical"),
    ([r"\bpopulation\b", r"\bcohort\b", r"\batlas\b"], "Population"),
    ([r"\bbiobank\b", r"\ball of us\b"], "Biobank"),
    ([r"\bbenchmark\b", r"\bcomparative\b", r"\bcomparison\b", r"\bpilot\b"], "Benchmark"),
    ([r"\bmethylation\b"], "Methylation"),
    ([r"\bsingle-cell\b", r"\bsingle cell\b"], "Single Cell"),
    ([r"\bhifi\b"], "HiFi"),
    ([r"\bont\b", r"\bnanopore\b", r"\boxford nanopore\b"], "ONT"),
    (
        [r"\bstructural variation\b", r"\bstructural variants?\b", r"\bsvs?\b"],
        "Structural Variation",
    ),
    ([r"\bbrain\b", r"\bcerebral\b", r"\bforebrain\b", r"\bcortical\b", r"\btelencephalic\b"], "Brain"),
    (
        [r"\bintestinal\b", r"\bgastrointestinal\b", r"\bcolon\b", r"\bcolonic\b", r"\bcolitis\b"],
        "Colon / Intestine",
    ),
    ([r"\bkidney\b", r"\bnephron\b", r"\bnephric\b", r"\bproximal tubule\b", r"\bureteric bud\b"], "Kidney"),
    ([r"\bheart\b", r"\bcardiac\b", r"\bheart-forming\b"], "Heart"),
    ([r"\bliver\b", r"\bhepatic\b", r"\bhepatocyte\b"], "Liver"),
    ([r"\bpancreas\b", r"\bpancreatic\b", r"\bbiliary\b"], "Pancreas / Biliary"),
    ([r"\blung\b", r"\bpulmonary\b", r"\binterstitial lung disease\b"], "Lung"),
    ([r"\bbreast\b"], "Breast"),
    ([r"\bprostate\b"], "Prostate"),
    ([r"\btumou?r\b", r"\bcancer\b", r"\bdrug screening\b", r"\bdrug-screening\b"], "Tumor / Cancer"),
    ([r"\bassembloid\b", r"\bassembly\b"], "Assembloid"),
    ([r"\bmigration\b", r"\binterneuron\b"], "Neuronal Migration"),
    (
        [r"\bair.?liquid interface\b", r"\bali(?:-co)?\b", r"\bslice culture\b"],
        "ALI Slice Culture",
    ),
    ([r"\blong-term culture\b", r"\bneuronal maturation\b", r"\bmaturation\b"], "Long-Term Maturation"),
    ([r"\bcrisp?r\b", r"\bknockin\b", r"\bknockout\b", r"\bgene editing\b"], "Gene Editing"),
    ([r"\btransplantation\b", r"\bxenotransplantation\b"], "Transplantation"),
    ([r"\bcoculture\b", r"\bco-culture\b", r"\bmicrobes?\b", r"\bt-cell\b"], "Coculture"),
]

GRAPH_TAG_EXCLUDES = {
    "Paper",
    "Article",
    "Book",
    "Dataset",
    "Other",
    "Queued",
    "Open",
    "Ingested",
    "Core",
    "Concept",
    "Query",
    "Synthesis",
}

GRAPH_GROUP_PRIORITY = [
    "Brain",
    "Colon / Intestine",
    "Kidney",
    "Heart",
    "Liver",
    "Pancreas / Biliary",
    "Lung",
    "Tumor / Cancer",
    "Breast",
    "Prostate",
    "Rare Disease",
    "Clinical",
    "Population",
    "Single Cell",
    "Structural Variation",
    "Benchmark",
    "Methylation",
    "HiFi",
    "ONT",
    "Biobank",
    "Assembloid",
    "Neuronal Migration",
    "ALI Slice Culture",
    "Long-Term Maturation",
    "Gene Editing",
    "Transplantation",
    "Coculture",
]

GRAPH_GROUP_PALETTE = [
    "#7a3c2d",
    "#35636b",
    "#6d5c2c",
    "#6d3a5b",
    "#47643e",
    "#5e4b7e",
    "#315f7d",
    "#7a4f2e",
    "#6a3651",
    "#4f5f2d",
]

GRAPH_THEME_PHRASES = {
    "Brain": {"en": "brain region or lineage focus", "ko": "뇌 영역 또는 계통 초점"},
    "Colon / Intestine": {"en": "gut lineage or intestinal context", "ko": "장 계통 또는 장기 맥락"},
    "Kidney": {"en": "kidney segment or nephron context", "ko": "신장 분절 또는 nephron 맥락"},
    "Heart": {"en": "cardiac lineage or heart-forming context", "ko": "심장 계통 또는 심장 형성 맥락"},
    "Liver": {"en": "hepatic differentiation context", "ko": "간 분화 맥락"},
    "Pancreas / Biliary": {"en": "pancreatic or biliary lineage focus", "ko": "췌장 또는 담도 계통 초점"},
    "Lung": {"en": "lung lineage or airway context", "ko": "폐 계통 또는 기도 맥락"},
    "Tumor / Cancer": {"en": "tumor or patient-derived disease context", "ko": "종양 또는 환자 유래 질환 맥락"},
    "Breast": {"en": "breast organoid context", "ko": "유방 오가노이드 맥락"},
    "Prostate": {"en": "prostate organoid context", "ko": "전립선 오가노이드 맥락"},
    "Rare Disease": {"en": "rare-disease diagnostic setting", "ko": "희귀질환 진단 맥락"},
    "Clinical": {"en": "clinical interpretation", "ko": "임상 해석"},
    "Population": {"en": "population or cohort scale", "ko": "집단 또는 코호트 규모"},
    "Single Cell": {"en": "single-cell readout", "ko": "단일세포 분석"},
    "Structural Variation": {"en": "structural-variation focus", "ko": "구조변이 초점"},
    "Benchmark": {"en": "benchmark or comparison design", "ko": "벤치마크 또는 비교 설계"},
    "Methylation": {"en": "methylation readout", "ko": "메틸레이션 readout"},
    "HiFi": {"en": "PacBio HiFi platform choice", "ko": "PacBio HiFi 플랫폼 선택"},
    "ONT": {"en": "Oxford Nanopore platform choice", "ko": "Oxford Nanopore 플랫폼 선택"},
    "Biobank": {"en": "biobank-scale sampling", "ko": "바이오뱅크 규모 샘플링"},
    "Assembloid": {"en": "assembloid architecture", "ko": "어셈블로이드 구조"},
    "Neuronal Migration": {"en": "neuronal migration biology", "ko": "신경세포 이동 생물학"},
    "ALI Slice Culture": {"en": "ALI or slice-culture maturation strategy", "ko": "ALI 또는 슬라이스 배양 성숙화 전략"},
    "Long-Term Maturation": {"en": "long-term maturation strategy", "ko": "장기 성숙화 전략"},
    "Gene Editing": {"en": "gene-editing workflow", "ko": "유전자 편집 워크플로"},
    "Transplantation": {"en": "transplantation assay context", "ko": "이식 실험 맥락"},
    "Coculture": {"en": "coculture or microenvironment setup", "ko": "공배양 또는 미세환경 설정"},
    "Other Papers": {"en": "paper-specific shared context", "ko": "논문별 공통 맥락"},
}


@dataclass
class Page:
    source_path: Path
    output_path: Path
    rel_source: Path
    rel_output: Path
    section: str
    section_label: str
    title: str
    meta_items: List[Tuple[str, str]]
    meta_dict: Dict[str, str]
    raw_body: str
    content: str
    excerpt: str
    tags: List[str]
    outgoing_links: List[str]
    year: Optional[int]


def parse_frontmatter(text: str) -> Tuple[Dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text

    parts = text.split("\n")
    try:
        end_index = parts[1:].index("---") + 1
    except ValueError:
        return {}, text

    metadata: Dict[str, str] = {}
    for line in parts[1:end_index]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    body = "\n".join(parts[end_index + 1 :])
    return metadata, body


def slugify(text: str) -> str:
    lowered = text.strip().lower()
    lowered = re.sub(r"[^\w\s-]", "", lowered)
    lowered = re.sub(r"[\s_]+", "-", lowered)
    lowered = re.sub(r"-+", "-", lowered)
    return lowered.strip("-") or "section"


def output_rel_for_source(rel_source: Path) -> Path:
    if rel_source.as_posix() == "index.md":
        return Path("index-page.html")
    return rel_source.with_suffix(".html")


def convert_markdown_target(target: str) -> str:
    if target.startswith(("http://", "https://", "mailto:", "#", "/")):
        return target

    anchor = ""
    base = target
    if "#" in target:
        base, anchor = target.split("#", 1)
        anchor = "#" + slugify(anchor)

    if base.endswith(".md"):
        path_obj = Path(base)
        if path_obj.name == "index.md":
            converted = path_obj.with_name("index-page.html").as_posix()
        else:
            converted = path_obj.with_suffix(".html").as_posix()
        return converted + anchor

    return target


def render_plain_text(text: str) -> str:
    text = html.escape(text)
    text = BOLD_RE.sub(r"<strong>\1</strong>", text)
    text = ITALIC_RE.sub(r"<em>\1</em>", text)
    return text


def render_inline(text: str) -> str:
    chunks = text.split("`")
    rendered: List[str] = []

    for index, chunk in enumerate(chunks):
        if index % 2 == 1:
            rendered.append("<code>%s</code>" % html.escape(chunk))
            continue

        cursor = 0
        part_output: List[str] = []
        for match in LINK_RE.finditer(chunk):
            part_output.append(render_plain_text(chunk[cursor : match.start()]))
            label = render_plain_text(match.group(1))
            href = html.escape(convert_markdown_target(match.group(2)), quote=True)
            part_output.append('<a href="%s">%s</a>' % (href, label))
            cursor = match.end()
        part_output.append(render_plain_text(chunk[cursor:]))
        rendered.append("".join(part_output))

    return "".join(rendered)


def render_markdown(body: str) -> str:
    html_parts: List[str] = []
    paragraph_lines: List[str] = []
    list_type = None
    list_items: List[str] = []
    in_code = False
    code_lines: List[str] = []

    def flush_paragraph():
        nonlocal paragraph_lines
        if paragraph_lines:
            text = " ".join(line.strip() for line in paragraph_lines)
            html_parts.append("<p>%s</p>" % render_inline(text))
            paragraph_lines = []

    def flush_list():
        nonlocal list_type, list_items
        if list_type and list_items:
            tag = "ul" if list_type == "ul" else "ol"
            items = "".join("<li>%s</li>" % item for item in list_items)
            html_parts.append("<%s>%s</%s>" % (tag, items, tag))
        list_type = None
        list_items = []

    def flush_code():
        nonlocal code_lines
        if code_lines:
            code_text = html.escape("\n".join(code_lines))
            html_parts.append("<pre><code>%s</code></pre>" % code_text)
            code_lines = []

    for raw_line in body.splitlines():
        line = raw_line.rstrip("\n")
        stripped = line.strip()

        if stripped.startswith("```"):
            flush_paragraph()
            flush_list()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
                code_lines = []
            continue

        if in_code:
            code_lines.append(line)
            continue

        if not stripped:
            flush_paragraph()
            flush_list()
            continue

        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            flush_paragraph()
            flush_list()
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()
            heading_id = slugify(re.sub(r"[\[\]]", "", heading_text))
            html_parts.append(
                "<h%s id=\"%s\">%s</h%s>"
                % (level, heading_id, render_inline(heading_text), level)
            )
            continue

        if stripped.startswith("> "):
            flush_paragraph()
            flush_list()
            html_parts.append("<blockquote><p>%s</p></blockquote>" % render_inline(stripped[2:]))
            continue

        unordered_match = UNORDERED_LIST_RE.match(stripped)
        if unordered_match:
            flush_paragraph()
            if list_type not in (None, "ul"):
                flush_list()
            list_type = "ul"
            list_items.append(render_inline(unordered_match.group(1)))
            continue

        ordered_match = ORDERED_LIST_RE.match(stripped)
        if ordered_match:
            flush_paragraph()
            if list_type not in (None, "ol"):
                flush_list()
            list_type = "ol"
            list_items.append(render_inline(ordered_match.group(1)))
            continue

        paragraph_lines.append(stripped)

    flush_paragraph()
    flush_list()
    if in_code:
        flush_code()

    return "\n".join(html_parts)


def discover_markdown_files() -> List[Path]:
    return sorted(
        path
        for path in WIKI_DIR.rglob("*.md")
        if path.is_file() and not any(part.startswith(".") for part in path.parts)
    )


def extract_title(metadata: Dict[str, str], body: str, path: Path) -> str:
    if metadata.get("title"):
        return metadata["title"]
    for line in body.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def strip_markdown_syntax(text: str) -> str:
    text = LINK_RE.sub(r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"[*_#>-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_section_block(body: str, section_title: str) -> str:
    capture = False
    captured: List[str] = []
    heading_level = None
    target_slug = slugify(section_title)

    for raw_line in body.splitlines():
        stripped = raw_line.strip()
        heading_match = HEADING_RE.match(stripped)
        if heading_match:
            level = len(heading_match.group(1))
            heading_slug = slugify(heading_match.group(2).strip())
            if capture and heading_level is not None and level <= heading_level:
                break
            if heading_slug == target_slug:
                capture = True
                heading_level = level
                continue
        if capture:
            captured.append(raw_line)

    return "\n".join(captured).strip()


def extract_excerpt(body: str, title: str) -> str:
    candidates: List[str] = []
    summary_block = extract_section_block(body, "Summary")
    if summary_block:
        candidates.extend(summary_block.splitlines())
    else:
        candidates.extend(body.splitlines())

    cleaned: List[str] = []
    for line in candidates:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped == "# %s" % title:
            continue
        if stripped.startswith("#"):
            continue
        text = strip_markdown_syntax(stripped)
        if text:
            cleaned.append(text)
        if len(cleaned) == 2:
            break

    return " ".join(cleaned) if cleaned else title


def resolve_internal_link(current_rel_source: Path, target: str) -> Optional[Path]:
    if target.startswith(("http://", "https://", "mailto:", "#", "/")):
        return None

    base = target.split("#", 1)[0]
    if not base.endswith(".md"):
        return None

    candidate = (WIKI_DIR / current_rel_source.parent / base).resolve()
    try:
        return candidate.relative_to(WIKI_DIR)
    except ValueError:
        return None


def extract_related_concept_tags(body: str) -> List[str]:
    related_block = extract_section_block(body, "Related concepts")
    if not related_block:
        return []

    labels = []
    for label, target in LINK_RE.findall(related_block):
        if target.endswith(".md") or ".md#" in target:
            labels.append(label.strip())
    return labels


def infer_keyword_tags(text: str) -> List[str]:
    lowered = text.lower()
    tags = []
    for patterns, label in KEYWORD_TAGS:
        if any(re.search(pattern, lowered) for pattern in patterns):
            tags.append(label)
    return tags


def extract_graph_tags(tags: List[str]) -> List[str]:
    graph_tags = []
    for tag in tags:
        if tag in GRAPH_TAG_EXCLUDES:
            continue
        if tag.isdigit():
            continue
        graph_tags.append(tag)
    return graph_tags


def choose_graph_group(graph_tags: List[str]) -> str:
    for label in GRAPH_GROUP_PRIORITY:
        if label in graph_tags:
            return label
    if graph_tags:
        return graph_tags[0]
    return "Other Papers"


def format_readable_list(items: List[str], language: str) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        joiner = " and " if language == "en" else "와 "
        return f"{items[0]}{joiner}{items[1]}"
    if language == "en":
        return ", ".join(items[:-1]) + f", and {items[-1]}"
    return ", ".join(items[:-1]) + f", 그리고 {items[-1]}"


def build_graph_copy(paper_pages: List[Dict[str, object]]) -> Dict[str, Dict[str, str]]:
    metadata = read_collection_metadata(ROOT)
    graph_copy_meta = metadata.get("graph_copy")
    if isinstance(graph_copy_meta, dict) and "en" in graph_copy_meta and "ko" in graph_copy_meta:
        return graph_copy_meta

    theme_counts: Dict[str, int] = {}
    for page in paper_pages:
        for tag in set(page.get("graph_tags") or []):
            if tag == "Other Papers":
                continue
            if tag not in GRAPH_THEME_PHRASES:
                continue
            theme_counts[tag] = theme_counts.get(tag, 0) + 1

    top_groups = [
        label
        for label, _count in sorted(
            theme_counts.items(),
            key=lambda item: (-item[1], GRAPH_GROUP_PRIORITY.index(item[0]) if item[0] in GRAPH_GROUP_PRIORITY else 999, item[0].lower()),
        )
        if _count > 1
    ]
    if not top_groups:
        top_groups = [
            str(page.get("graph_group") or "Other Papers")
            for page in paper_pages
            if page.get("graph_group")
        ]

    theme_phrases_en = [
        GRAPH_THEME_PHRASES.get(label, {}).get("en", label.lower())
        for label in top_groups[:4]
    ]
    theme_phrases_ko = [
        GRAPH_THEME_PHRASES.get(label, {}).get("ko", label)
        for label in top_groups[:4]
    ]

    if not theme_phrases_en:
        theme_phrases_en = ["shared paper themes"]
        theme_phrases_ko = ["공통 논문 주제"]

    return {
        "en": {
            "graph_toolbar": (
                "Only paper nodes are shown here. Edges represent direct paper links or shared themes such as "
                f"{format_readable_list(theme_phrases_en, 'en')}."
            ),
            "graph_detail_help": (
                "This graph uses a force-directed layout. Drag nodes, pan the canvas, zoom with the wheel, "
                "tune node size, edge width, label density, repulsion, link distance, and label visibility with the "
                "controls, and treat thicker or darker edges as stronger relationships."
            ),
        },
        "ko": {
            "graph_toolbar": (
                "여기에는 논문 노드만 표시됩니다. 선은 직접 논문 링크이거나 "
                f"{format_readable_list(theme_phrases_ko, 'ko')} 같은 공통 주제를 뜻합니다."
            ),
            "graph_detail_help": (
                "이 그래프는 force-directed 레이아웃을 사용합니다. 노드를 드래그하고, 화면을 이동하고, "
                "휠로 확대·축소할 수 있으며, 컨트롤로 노드 크기, 엣지 두께, 라벨 밀도, 반발력, 링크 거리, "
                "라벨 표시 여부를 조절할 수 있습니다. "
                "더 두껍거나 진한 선일수록 연관성이 더 강합니다."
            ),
        },
    }


def build_paper_relationships(serialized_pages: List[Dict[str, object]]) -> List[Dict[str, object]]:
    papers = [page for page in serialized_pages if page["section"] == "sources"]
    tag_frequency: Dict[str, int] = {}
    for page in papers:
        for tag in set(page["graph_tags"]):
            tag_frequency[tag] = tag_frequency.get(tag, 0) + 1

    common_tag_cutoff = max(4, math.ceil(len(papers) * 0.5))
    edges: List[Dict[str, object]] = []

    for index, source in enumerate(papers):
        source_graph_tags = set(source["graph_tags"])
        source_links = set(source["source_links"])
        for target in papers[index + 1 :]:
            target_graph_tags = set(target["graph_tags"])
            target_links = set(target["source_links"])
            direct_link = target["id"] in source_links or source["id"] in target_links
            shared_tags = sorted(
                tag
                for tag in (source_graph_tags & target_graph_tags)
                if tag_frequency.get(tag, 0) <= common_tag_cutoff
            )
            if not direct_link and not shared_tags:
                continue

            reasons: List[str] = []
            if direct_link:
                reasons.append("Direct Wiki Link")
            reasons.extend(shared_tags[:4])
            edges.append(
                {
                    "source": source["id"],
                    "target": target["id"],
                    "strength": len(shared_tags) + (2 if direct_link else 0),
                    "reasons": reasons,
                }
            )

    return sorted(
        edges,
        key=lambda item: (-item["strength"], item["source"], item["target"]),
    )


def extract_year(rel_source: Path, metadata: Optional[Dict[str, str]] = None) -> Optional[int]:
    if metadata:
        explicit_year = metadata.get("year", "").strip()
        if explicit_year.isdigit() and len(explicit_year) == 4:
            return int(explicit_year)

        published_date = metadata.get("published_date", "").strip()
        published_match = re.match(r"^(19|20)\d{2}", published_date)
        if published_match:
            return int(published_match.group(0))

    stem = rel_source.stem
    match = re.search(r"(?<!\d)(19|20)\d{2}(?!\d)", stem)
    if match:
        return int(match.group(0))
    return None


def resolve_article_href(metadata: Dict[str, str]) -> str:
    doi_url = metadata.get("doi_url", "").strip()
    if doi_url:
        return doi_url

    doi = metadata.get("doi", "").strip()
    if doi:
        return f"https://doi.org/{doi}"

    article_url = metadata.get("article_url", "").strip()
    if article_url:
        return article_url

    return ""


def build_page(path: Path) -> Page:
    rel_source = path.relative_to(WIKI_DIR)
    rel_output = output_rel_for_source(rel_source)
    output_path = OUTPUT_DIR / rel_output
    section = rel_source.parts[0] if len(rel_source.parts) > 1 else ""
    section_label = SECTION_LABELS.get(section, section.title() or "Core")

    text = path.read_text(encoding="utf-8")
    metadata, body = parse_frontmatter(text)
    title = extract_title(metadata, body, path)

    body_lines = body.splitlines()
    first_content_index = 0
    while first_content_index < len(body_lines) and not body_lines[first_content_index].strip():
        first_content_index += 1
    if (
        first_content_index < len(body_lines)
        and body_lines[first_content_index].strip() == "# %s" % title
    ):
        body = "\n".join(body_lines[:first_content_index] + body_lines[first_content_index + 1 :]).lstrip()

    meta_items = [(key.replace("_", " "), value) for key, value in metadata.items()]

    source_block = extract_section_block(body, "Source")
    scope_line = ""
    for line in source_block.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("- scope:"):
            scope_line = stripped.split(":", 1)[1].strip()
            break

    excerpt = extract_excerpt(body, title)
    related_tags = extract_related_concept_tags(body)

    tag_set = {SECTION_TAGS.get(section, section_label)}
    if metadata.get("kind"):
        tag_set.add(metadata["kind"].title())
    if metadata.get("status"):
        tag_set.add(metadata["status"].title())
    tag_set.update(related_tags)
    tag_set.update(infer_keyword_tags(" ".join([title, excerpt, scope_line, body])))

    year = extract_year(rel_source, metadata)
    if year:
        tag_set.add(str(year))

    outgoing_links: List[str] = []
    for _, target in LINK_RE.findall(body):
        resolved = resolve_internal_link(rel_source, target)
        if resolved is not None:
            outgoing_links.append(resolved.as_posix())

    return Page(
        source_path=path,
        output_path=output_path,
        rel_source=rel_source,
        rel_output=rel_output,
        section=section,
        section_label=section_label,
        title=title,
        meta_items=meta_items,
        meta_dict=metadata,
        raw_body=body,
        content=render_markdown(body),
        excerpt=excerpt,
        tags=sorted(tag_set, key=lambda item: (item.isdigit(), item.lower())),
        outgoing_links=sorted(set(outgoing_links)),
        year=year,
    )


def build_navigation(pages: List[Page], current_page: Page):
    grouped = []
    dashboard_href = Path(os.path.relpath(OUTPUT_DIR / "index.html", current_page.output_path.parent)).as_posix()
    dashboard_file_href = (OUTPUT_DIR / "index.html").resolve().as_uri()
    dashboard_http_href = http_href_for_path(OUTPUT_DIR / "index.html")

    for section in SECTION_ORDER:
        items = [page for page in pages if page.section == section]
        if not items and section != "":
            continue

        section_items = []
        if section == "":
            section_items.append(
                {
                    "title": "Dashboard",
                    "href": dashboard_href,
                    "file_href": dashboard_file_href,
                    "http_href": dashboard_http_href,
                    "current": False,
                }
            )
        for page in items:
            href = Path(os.path.relpath(page.output_path, current_page.output_path.parent)).as_posix()
            section_items.append(
                {
                    "title": page.title,
                    "href": href,
                    "file_href": page.output_path.resolve().as_uri(),
                    "http_href": http_href_for_path(page.output_path),
                    "current": page.output_path == current_page.output_path,
                }
            )
        grouped.append({"label": SECTION_LABELS[section], "entries": section_items})
    return grouped


def serialize_page(page: Page) -> Dict[str, object]:
    raw_source = page.meta_dict.get("raw_source", "")
    article_href = resolve_article_href(page.meta_dict)
    pdf_href = ""
    pdf_file_href = ""
    pdf_http_href = ""
    if raw_source and (not PUBLIC_SITE_MODE or PUBLIC_SITE_INCLUDE_PDFS):
        pdf_href = (Path("..") / Path(raw_source)).as_posix()
        pdf_file_href = (ROOT / raw_source).resolve().as_uri()
        pdf_http_href = http_href_for_path(ROOT / raw_source)

    short_title = page.title
    if len(short_title) > 28:
        short_title = short_title[:25].rstrip() + "..."

    search_blob = " ".join(
        [
            page.title,
            page.excerpt,
            " ".join(page.tags),
            strip_markdown_syntax(page.raw_body),
            " ".join(value for _, value in page.meta_items),
        ]
    ).lower()

    source_links = [
        target
        for target in page.outgoing_links
        if target.startswith("sources/")
    ]
    graph_tags = extract_graph_tags(page.tags)

    return {
        "id": page.rel_source.as_posix(),
        "title": page.title,
        "short_title": short_title,
        "href": page.rel_output.as_posix(),
        "file_href": page.output_path.resolve().as_uri(),
        "http_href": http_href_for_path(page.output_path),
        "section": page.section,
        "section_label": page.section_label,
        "kind": page.meta_dict.get("kind", "").title(),
        "status": page.meta_dict.get("status", "").title(),
        "excerpt": page.excerpt,
        "tags": page.tags,
        "tags_norm": [slugify(tag) for tag in page.tags],
        "pdf_href": pdf_href,
        "pdf_file_href": pdf_file_href,
        "pdf_http_href": pdf_http_href,
        "article_href": article_href,
        "search_text": search_blob,
        "year": page.year,
        "sort_timestamp": int(page.source_path.stat().st_mtime),
        "graph_tags": graph_tags,
        "source_links": source_links,
    }


def render_dashboard_link_attrs(href: str, file_href: str = "", http_href: str = "") -> str:
    attrs = [f'href="{html.escape(href or "#", quote=True)}"']
    if file_href:
        attrs.append(f'data-file-href="{html.escape(file_href, quote=True)}"')
    if http_href:
        attrs.append(f'data-http-href="{html.escape(http_href, quote=True)}"')
    return " ".join(attrs)


def render_external_link_attrs(href: str) -> str:
    safe_href = html.escape(href or "#", quote=True)
    return f'href="{safe_href}" target="_blank" rel="noreferrer"'


def dashboard_year_label(page: Dict[str, object]) -> str:
    year = page.get("year")
    return str(year) if year else "Unspecified"


def dashboard_status_label(page: Dict[str, object]) -> str:
    return str(page.get("status") or "Unspecified")


def dashboard_theme_label(page: Dict[str, object]) -> str:
    return str(page.get("graph_group") or "Other")


def render_initial_paper_grid(paper_pages: List[Dict[str, object]]) -> str:
    cards = []
    sorted_papers = sorted(
        paper_pages,
        key=lambda page: (-(page.get("year") or 0), str(page.get("title", "")).lower()),
    )
    for paper in sorted_papers:
        tag_html = "".join(
            f'<span class="mini-chip">{html.escape(str(tag))}</span>'
            for tag in list(paper.get("tags", []))[:8]
        )
        pdf_link = ""
        if paper.get("pdf_href"):
            pdf_link = (
                f'<a class="card-link secondary" '
                f'{render_dashboard_link_attrs(str(paper.get("pdf_href", "")), str(paper.get("pdf_file_href", "")), str(paper.get("pdf_http_href", "")))}>'
                f'Open PDF</a>'
            )
        article_link = ""
        if paper.get("article_href"):
            article_link = (
                f'<a class="card-link tertiary" '
                f'{render_external_link_attrs(str(paper.get("article_href", "")))}>'
                f'Journal Page</a>'
            )
        cards.append(
            "\n".join(
                [
                    '<article class="paper-card">',
                    '  <div class="card-topline">',
                    f'    <span class="section-pill section-{html.escape(str(paper.get("section") or "core"))}">{html.escape(str(paper.get("section_label") or ""))}</span>',
                    f'    <span class="year-pill">{html.escape(str(paper.get("year") or ""))}</span>',
                    "  </div>",
                    f'  <h2>{html.escape(str(paper.get("title") or ""))}</h2>',
                    f'  <p class="card-excerpt">{html.escape(str(paper.get("excerpt") or ""))}</p>',
                    f'  <div class="card-tags">{tag_html}</div>',
                    '  <div class="card-actions">',
                    f'    <a class="card-link" {render_dashboard_link_attrs(str(paper.get("href", "")), str(paper.get("file_href", "")), str(paper.get("http_href", "")))}>Open Page</a>',
                    f"    {article_link}",
                    f"    {pdf_link}",
                    "  </div>",
                    "</article>",
                ]
            )
        )
    return "\n".join(cards)


def render_initial_page_list(serialized_pages: List[Dict[str, object]]) -> str:
    rows = []
    sorted_pages = sorted(
        serialized_pages,
        key=lambda page: (str(page.get("section_label") or ""), str(page.get("title") or "").lower()),
    )
    for page in sorted_pages:
        tag_html = "".join(
            f'<span class="mini-chip">{html.escape(str(tag))}</span>'
            for tag in list(page.get("tags", []))[:6]
        )
        rows.append(
            "\n".join(
                [
                    '<article class="page-row">',
                    '  <div class="page-row-main">',
                    '    <div class="page-row-head">',
                    f'      <span class="section-pill section-{html.escape(str(page.get("section") or "core"))}">{html.escape(str(page.get("section_label") or ""))}</span>',
                    f'      <a class="page-row-link" {render_dashboard_link_attrs(str(page.get("href", "")), str(page.get("file_href", "")), str(page.get("http_href", "")))}>{html.escape(str(page.get("title") or ""))}</a>',
                    "    </div>",
                    f'    <p class="page-row-excerpt">{html.escape(str(page.get("excerpt") or ""))}</p>',
                    f'    <div class="card-tags">{tag_html}</div>',
                    "  </div>",
                    '  <div class="page-row-actions">',
                    f'    <a class="card-link" {render_dashboard_link_attrs(str(page.get("href", "")), str(page.get("file_href", "")), str(page.get("http_href", "")))}>Open</a>',
                    "  </div>",
                    "</article>",
                ]
            )
        )
    return "\n".join(rows)


def render_initial_database(serialized_pages: List[Dict[str, object]]) -> Tuple[str, str]:
    rows = sorted(
        serialized_pages,
        key=lambda page: (-(page.get("sort_timestamp") or 0), str(page.get("title") or "").lower()),
    )
    years = [page.get("year") for page in rows if page.get("year")]
    year_range = f"{min(years)}-{max(years)}" if years else "Unspecified"
    summary_html = (
        f'<span class="summary-chip"><strong>{len(rows)}</strong><span>Rows</span></span>'
        f'<span class="summary-chip"><strong>{sum(1 for page in rows if page.get("section") == "sources")}</strong><span>Papers</span></span>'
        f'<span class="summary-chip"><strong>{html.escape(year_range)}</strong><span>Year Range</span></span>'
        f'<span class="summary-chip"><strong>1</strong><span>Groups</span></span>'
    )

    row_html = []
    for page in rows:
        tags_html = "".join(
            f'<span class="mini-chip">{html.escape(str(tag))}</span>'
            for tag in list(page.get("tags", []))[:4]
        )
        pdf_link = ""
        if page.get("pdf_href"):
            pdf_link = (
                f'<a class="table-action secondary" '
                f'{render_dashboard_link_attrs(str(page.get("pdf_href", "")), str(page.get("pdf_file_href", "")), str(page.get("pdf_http_href", "")))}>'
                f'Open PDF</a>'
            )
        article_link = ""
        if page.get("article_href"):
            article_link = (
                f'<a class="table-action tertiary" '
                f'{render_external_link_attrs(str(page.get("article_href", "")))}>'
                f'Journal Page</a>'
            )
        row_html.append(
            "\n".join(
                [
                    "<tr>",
                    '  <td class="database-title-cell">',
                    f'    <a class="database-title-link" {render_dashboard_link_attrs(str(page.get("href", "")), str(page.get("file_href", "")), str(page.get("http_href", "")))}>{html.escape(str(page.get("title") or ""))}</a>',
                    f'    <p class="database-subtle">{html.escape(str(page.get("excerpt") or ""))}</p>',
                    "  </td>",
                    f'  <td><span class="section-pill section-{html.escape(str(page.get("section") or "core"))}">{html.escape(str(page.get("section_label") or ""))}</span></td>',
                    f'  <td>{html.escape(dashboard_year_label(page))}</td>',
                    f'  <td>{html.escape(dashboard_status_label(page))}</td>',
                    f'  <td>{html.escape(dashboard_theme_label(page))}</td>',
                    f'  <td>{int(page.get("relation_count") or 0)}</td>',
                    f'  <td><div class="database-tag-cell">{tags_html}</div></td>',
                    '  <td><div class="database-actions">',
                    f'    <a class="table-action" {render_dashboard_link_attrs(str(page.get("href", "")), str(page.get("file_href", "")), str(page.get("http_href", "")))}>Open</a>',
                    f"    {article_link}",
                    f"    {pdf_link}",
                    "  </div></td>",
                    "</tr>",
                ]
            )
        )

    groups_html = (
        '<section class="database-group">'
        '<div class="database-table-wrap">'
        '<table class="database-table">'
        '<thead><tr>'
        '<th>Title</th><th>Section</th><th>Year</th><th>Status</th><th>Theme</th><th>Relations</th><th>Tags</th><th>Actions</th>'
        '</tr></thead>'
        f"<tbody>{''.join(row_html)}</tbody>"
        "</table></div></section>"
    )
    return summary_html, groups_html


def render_initial_graph_svg(
    paper_pages: List[Dict[str, object]],
    paper_edges: List[Dict[str, object]],
) -> str:
    if not paper_pages:
        return (
            f'<text x="{GRAPH_VIEWBOX_WIDTH / 2}" y="{GRAPH_VIEWBOX_HEIGHT / 2}" '
            'text-anchor="middle" class="graph-empty">No papers available.</text>'
        )

    degrees: Dict[str, int] = {str(page["id"]): 0 for page in paper_pages}
    for edge in paper_edges:
        strength = int(edge.get("strength") or 1)
        degrees[str(edge["source"])] = degrees.get(str(edge["source"]), 0) + strength
        degrees[str(edge["target"])] = degrees.get(str(edge["target"]), 0) + strength

    groups = sorted(
        {str(page.get("graph_group") or "Other Papers") for page in paper_pages},
        key=lambda label: (
            GRAPH_GROUP_PRIORITY.index(label) if label in GRAPH_GROUP_PRIORITY else len(GRAPH_GROUP_PRIORITY),
            label.lower(),
        ),
    )
    center_x = GRAPH_VIEWBOX_WIDTH / 2
    center_y = GRAPH_VIEWBOX_HEIGHT / 2
    anchor_radius = 245 if len(groups) > 1 else 0

    anchors: Dict[str, Tuple[float, float]] = {}
    if len(groups) <= 1:
        anchors[groups[0]] = (center_x, center_y)
    else:
        for index, group in enumerate(groups):
            angle = (math.pi * 2 * index) / len(groups) - math.pi / 2
            anchors[group] = (
                center_x + math.cos(angle) * anchor_radius,
                center_y + math.sin(angle) * 205,
            )

    grouped_pages: Dict[str, List[Dict[str, object]]] = {group: [] for group in groups}
    for page in sorted(
        paper_pages,
        key=lambda item: (-degrees.get(str(item["id"]), 0), str(item.get("title") or "").lower()),
    ):
        grouped_pages[str(page.get("graph_group") or "Other Papers")].append(page)

    positions: Dict[str, Tuple[float, float]] = {}
    label_ids: set[str] = set()
    for group, pages in grouped_pages.items():
        anchor_x, anchor_y = anchors[group]
        total = len(pages)
        if total == 1:
            page = pages[0]
            positions[str(page["id"])] = (anchor_x, anchor_y)
            label_ids.add(str(page["id"]))
            continue

        ring_radius = min(104, 28 + total * 7.5)
        label_ids.add(str(pages[0]["id"]))
        for index, page in enumerate(pages):
            angle = (math.pi * 2 * index) / total - math.pi / 2
            positions[str(page["id"])] = (
                anchor_x + math.cos(angle) * ring_radius,
                anchor_y + math.sin(angle) * ring_radius,
            )

    ranked_ids = [
        str(page["id"])
        for page in sorted(
            paper_pages,
            key=lambda item: (-degrees.get(str(item["id"]), 0), str(item.get("title") or "").lower()),
        )
    ]
    max_labels = len(paper_pages) if len(paper_pages) <= 14 else 14
    label_ids.update(ranked_ids[:max_labels])

    edge_markup: List[str] = []
    for edge in paper_edges:
        source_id = str(edge["source"])
        target_id = str(edge["target"])
        if source_id not in positions or target_id not in positions:
            continue
        x1, y1 = positions[source_id]
        x2, y2 = positions[target_id]
        stroke_width = 0.8 + min(int(edge.get("strength") or 1), 7) * 0.42
        opacity = min(0.22 + int(edge.get("strength") or 1) * 0.08, 0.82)
        edge_markup.append(
            '<line class="graph-edge" '
            f'x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke-width="{stroke_width:.2f}" opacity="{opacity:.2f}"></line>'
        )

    node_markup: List[str] = []
    for page in paper_pages:
        page_id = str(page["id"])
        if page_id not in positions:
            continue
        x, y = positions[page_id]
        radius = max(4.2, (6 + min(5, math.sqrt(max(degrees.get(page_id, 1), 1)) * 1.2)) * 0.72)
        title = html.escape(str(page.get("title") or ""))
        short_title = html.escape(str(page.get("short_title") or title))
        href_attrs = render_dashboard_link_attrs(
            str(page.get("href") or ""),
            str(page.get("file_href") or ""),
            str(page.get("http_href") or ""),
        )
        label_markup = ""
        if page_id in label_ids:
            label_markup = (
                f'<text class="graph-label" x="{x:.1f}" y="{y + radius + 18:.1f}">{short_title}</text>'
            )
        node_markup.append(
            "\n".join(
                [
                    f'<a {href_attrs}>',
                    f'  <g class="graph-node static-node" transform="translate({x:.1f}, {y:.1f})">',
                    f'    <circle r="{radius:.2f}" fill="{html.escape(str(page.get("graph_color") or "#8e3c27"))}"></circle>',
                    f"    <title>{title}</title>",
                    "  </g>",
                    "</a>",
                    label_markup,
                ]
            )
        )

    return "\n".join(edge_markup + node_markup)


def build_dashboard_context(pages: List[Page]) -> Dict[str, object]:
    serialized_pages = [serialize_page(page) for page in pages]
    for page in serialized_pages:
        page["graph_group"] = choose_graph_group(page["graph_tags"])
    paper_pages = [page for page in serialized_pages if page["section"] == "sources"]

    graph_groups_sorted = sorted(
        {page["graph_group"] for page in paper_pages},
        key=lambda label: (
            GRAPH_GROUP_PRIORITY.index(label)
            if label in GRAPH_GROUP_PRIORITY
            else len(GRAPH_GROUP_PRIORITY),
            label.lower(),
        ),
    )
    group_colors = {
        label: GRAPH_GROUP_PALETTE[index % len(GRAPH_GROUP_PALETTE)]
        for index, label in enumerate(graph_groups_sorted)
    }
    for page in paper_pages:
        page["graph_color"] = group_colors[page["graph_group"]]

    paper_edges = build_paper_relationships(serialized_pages)
    relation_counts: Dict[str, int] = {}
    for edge in paper_edges:
        relation_counts[edge["source"]] = relation_counts.get(edge["source"], 0) + 1
        relation_counts[edge["target"]] = relation_counts.get(edge["target"], 0) + 1
    for page in serialized_pages:
        page["relation_count"] = max(relation_counts.get(page["id"], 0), len(page["source_links"]))

    tag_counts: Dict[str, int] = {}
    tag_labels: Dict[str, str] = {}
    for page in serialized_pages:
        for tag in page["tags"]:
            slug = slugify(tag)
            tag_counts[slug] = tag_counts.get(slug, 0) + 1
            tag_labels[slug] = tag

    tags = [
        {"slug": slug, "label": tag_labels[slug], "count": count}
        for slug, count in sorted(
            tag_counts.items(),
            key=lambda item: (-item[1], tag_labels[item[0]].lower()),
        )
    ]

    counts = {
        "pages": len(serialized_pages),
        "papers": len(paper_pages),
        "concepts": sum(1 for page in serialized_pages if page["section"] == "concepts"),
        "edges": len(paper_edges),
    }

    section_legend = []
    for section in SECTION_ORDER:
        section_legend.append(
            {
                "key": section or "core",
                "label": SECTION_LABELS[section],
                "color": SECTION_COLORS[section],
                "count": sum(1 for page in serialized_pages if page["section"] == section),
            }
        )

    dashboard_data = {
        "pages": serialized_pages,
        "paper_edges": paper_edges,
        "tags": tags,
        "sections": section_legend,
        "section_colors": SECTION_COLORS,
        "graph_groups": [
            {
                "label": label,
                "key": slugify(label),
                "color": group_colors[label],
                "count": sum(1 for page in paper_pages if page["graph_group"] == label),
            }
            for label in graph_groups_sorted
        ],
    }

    page_by_source = {page.rel_source.as_posix(): page for page in pages}
    quick_links = []
    for rel_source, label in [
        ("overview.md", "Overview"),
        ("index.md", "Index Note"),
        ("log.md", "Log"),
    ]:
        page = page_by_source.get(rel_source)
        if page is not None:
            quick_links.append(
                {
                    "href": page.rel_output.as_posix(),
                    "file_href": page.output_path.resolve().as_uri(),
                    "http_href": http_href_for_path(page.output_path),
                    "label": label,
                }
            )

    syntheses = sorted(
        [page for page in pages if page.section == "syntheses"],
        key=lambda item: item.rel_output.as_posix(),
        reverse=True,
    )
    if syntheses:
        quick_links.append(
            {
                "href": syntheses[0].rel_output.as_posix(),
                "file_href": syntheses[0].output_path.resolve().as_uri(),
                "http_href": http_href_for_path(syntheses[0].output_path),
                "label": "Latest Synthesis",
            }
        )

    initial_database_summary_html, initial_database_groups_html = render_initial_database(serialized_pages)

    return {
        "counts": counts,
        "section_legend": section_legend,
        "graph_groups": dashboard_data["graph_groups"],
        "dashboard_data_json": json.dumps(dashboard_data, ensure_ascii=False),
        "quick_links": quick_links,
        "graph_copy": build_graph_copy(paper_pages),
        "initial_paper_grid_html": render_initial_paper_grid(paper_pages),
        "initial_page_list_html": render_initial_page_list(serialized_pages),
        "initial_database_summary_html": initial_database_summary_html,
        "initial_database_groups_html": initial_database_groups_html,
        "initial_graph_svg_html": render_initial_graph_svg(paper_pages, paper_edges),
    }


def build_i18n_data_json(ui_overrides: Optional[Dict[str, Dict[str, str]]] = None) -> str:
    ui_payload = {language: dict(values) for language, values in UI_TRANSLATIONS.items()}
    if ui_overrides:
        for language, overrides in ui_overrides.items():
            if language not in ui_payload:
                ui_payload[language] = {}
            ui_payload[language].update(overrides)
    return json.dumps(
        {
            "ui": ui_payload,
            "labels": {"en": {}, **LABEL_TRANSLATIONS},
        },
        ensure_ascii=False,
    )


def render_dashboard(pages: List[Page], generated_at: str):
    dashboard_path = OUTPUT_DIR / "index.html"
    context = build_dashboard_context(pages)
    home_path = PROJECT_ROOT / "index.html"
    home_href = Path(os.path.relpath(home_path, dashboard_path.parent)).as_posix()
    html_text = DASHBOARD_TEMPLATE.render(
        counts=context["counts"],
        section_legend=context["section_legend"],
        graph_groups=context["graph_groups"],
        dashboard_data_json=context["dashboard_data_json"],
        quick_links=context["quick_links"],
        initial_paper_grid_html=context["initial_paper_grid_html"],
        initial_page_list_html=context["initial_page_list_html"],
        initial_database_summary_html=context["initial_database_summary_html"],
        initial_database_groups_html=context["initial_database_groups_html"],
        initial_graph_svg_html=context["initial_graph_svg_html"],
        workspace_title=WORKSPACE_TITLE,
        workspace_description=WORKSPACE_DESCRIPTION,
        show_local_viewer_link=not PUBLIC_SITE_MODE,
        i18n_data_json=build_i18n_data_json(context["graph_copy"]),
        home_href=home_href,
        home_file_href=home_path.resolve().as_uri(),
        home_http_href=http_href_for_path(home_path),
        graph_toolbar_default=context["graph_copy"]["en"]["graph_toolbar"],
        graph_detail_help_default=context["graph_copy"]["en"]["graph_detail_help"],
        dashboard_http_href=http_href_for_path(dashboard_path),
        generated_at=generated_at,
        site_brand=SITE_BRAND,
        logo_href=f"assets/{LOGO_FILENAME}",
    )
    dashboard_path.write_text(html_text, encoding="utf-8")


def render_page(page: Page, pages: List[Page], generated_at: str):
    page.output_path.parent.mkdir(parents=True, exist_ok=True)
    stylesheet_href = Path(os.path.relpath(STYLE_PATH, page.output_path.parent)).as_posix()
    logo_href = Path(os.path.relpath(ASSETS_DIR / LOGO_FILENAME, page.output_path.parent)).as_posix()
    dashboard_href = Path(os.path.relpath(OUTPUT_DIR / "index.html", page.output_path.parent)).as_posix()
    dashboard_file_href = (OUTPUT_DIR / "index.html").resolve().as_uri()
    dashboard_http_href = http_href_for_path(OUTPUT_DIR / "index.html")
    home_path = PROJECT_ROOT / "index.html"
    home_href = Path(os.path.relpath(home_path, page.output_path.parent)).as_posix()
    navigation = build_navigation(pages, page)
    html_text = PAGE_TEMPLATE.render(
        page=page,
        navigation=navigation,
        stylesheet_href=stylesheet_href,
        dashboard_href=dashboard_href,
        dashboard_file_href=dashboard_file_href,
        dashboard_http_href=dashboard_http_href,
        home_href=home_href,
        home_file_href=home_path.resolve().as_uri(),
        home_http_href=http_href_for_path(home_path),
        workspace_title=WORKSPACE_TITLE,
        workspace_description=WORKSPACE_DESCRIPTION,
        show_local_viewer_link=not PUBLIC_SITE_MODE,
        i18n_data_json=build_i18n_data_json(),
        generated_at=generated_at,
        site_brand=SITE_BRAND,
        logo_href=logo_href,
    )
    page.output_path.write_text(html_text, encoding="utf-8")


def render_site(pages: List[Page]):
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)

    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    STYLE_PATH.write_text(STYLE_TEXT.strip() + "\n", encoding="utf-8")
    if LOGO_SOURCE_PATH.exists():
        shutil.copy2(LOGO_SOURCE_PATH, ASSETS_DIR / LOGO_FILENAME)
    generated_at = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")

    for page in pages:
        render_page(page, pages, generated_at)
    render_dashboard(pages, generated_at)


ROOT_HUB_TEMPLATE = Template(
    """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{{ site_brand }} | Research Collection Hub</title>
  <style>
    :root {
      --paper: #f7f2e7;
      --panel: rgba(255, 252, 245, 0.88);
      --panel-strong: rgba(255, 250, 241, 0.95);
      --ink: #221d18;
      --muted: #6a6259;
      --accent: #7a3520;
      --accent-soft: #edd8c4;
      --line: rgba(77, 60, 44, 0.16);
      --shadow: 0 22px 60px rgba(45, 30, 17, 0.12);
      --font-sans: Arial, "Malgun Gothic", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
    }

    * { box-sizing: border-box; }

    html {
      min-height: 100%;
      background:
        radial-gradient(circle at top left, rgba(195, 128, 86, 0.18), transparent 28%),
        radial-gradient(circle at top right, rgba(117, 72, 52, 0.12), transparent 22%),
        linear-gradient(180deg, #f5ead9 0%, #efe3d0 100%);
    }

    body {
      margin: 0;
      color: var(--ink);
      font-family: var(--font-sans);
      line-height: 1.65;
    }

    a {
      color: var(--accent);
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    code {
      font-family: "SFMono-Regular", "Menlo", "Consolas", monospace;
      background: rgba(122, 53, 32, 0.08);
      border-radius: 0.35rem;
      padding: 0.15rem 0.35rem;
      font-size: 0.92em;
    }

    .page-shell {
      max-width: 1520px;
      margin: 0 auto;
      padding: 1.5rem;
    }

    .hub {
      display: grid;
      gap: 1.35rem;
    }

    .panel {
      backdrop-filter: blur(8px);
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 1.4rem;
      box-shadow: var(--shadow);
    }

    .eyebrow {
      margin: 0 0 0.45rem;
      color: var(--muted);
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.14em;
    }

    h1, h2, h3 {
      margin: 0;
      line-height: 1.08;
      font-weight: 700;
    }

    .hero {
      display: grid;
      grid-template-columns: minmax(0, 1.18fr) minmax(320px, 0.82fr);
      gap: 1.25rem;
      padding: 1.65rem 1.8rem;
    }

    .hero-brand {
      display: inline-flex;
      align-items: center;
      gap: 0.78rem;
      margin-bottom: 0.9rem;
      padding: 0.42rem 0.62rem 0.42rem 0.46rem;
      width: fit-content;
      border-radius: 999px;
      border: 1px solid rgba(77, 60, 44, 0.14);
      background: rgba(255, 255, 255, 0.78);
      box-shadow: 0 14px 28px rgba(53, 34, 19, 0.08);
      color: inherit;
    }

    .hero-brand:hover {
      text-decoration: none;
      background: rgba(255, 255, 255, 0.9);
    }

    .hero-brand img {
      width: 2rem;
      height: 2rem;
      border-radius: 0.7rem;
      flex: 0 0 auto;
    }

    .hero-brand-copy {
      display: grid;
      gap: 0.08rem;
      line-height: 1.1;
    }

    .hero-brand-copy strong {
      font-size: 0.92rem;
      letter-spacing: 0.04em;
    }

    .hero-brand-copy span {
      color: var(--muted);
      font-size: 0.7rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
    }

    .hero h1 {
      font-size: clamp(2.45rem, 4vw, 4rem);
      letter-spacing: -0.03em;
    }

    .lede {
      margin: 0.9rem 0 0;
      max-width: 62ch;
      color: #4e4740;
      font-size: 1.04rem;
    }

    .hero-actions {
      display: flex;
      flex-wrap: wrap;
      gap: 0.7rem;
      margin-top: 1rem;
    }

    .hero-button {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 0.68rem 0.96rem;
      border-radius: 999px;
      background: rgba(122, 53, 32, 0.1);
      border: 1px solid rgba(122, 53, 32, 0.16);
      color: #5d2618;
      font-weight: 700;
      text-decoration: none;
    }

    .hero-button:hover {
      text-decoration: none;
      background: rgba(122, 53, 32, 0.16);
    }

    .hero-stats {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0.9rem;
    }

    .stat-card, .collection-card, .note-panel {
      background: var(--panel-strong);
      border: 1px solid var(--line);
      box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.65);
    }

    .stat-card {
      border-radius: 1.1rem;
      padding: 1rem 1.05rem;
    }

    .stat-label {
      display: block;
      color: var(--muted);
      font-size: 0.82rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
    }

    .stat-card strong {
      display: block;
      margin-top: 0.35rem;
      font-size: 2rem;
      line-height: 1;
    }

    .section-panel {
      padding: 1.45rem 1.5rem 1.6rem;
    }

    .section-heading {
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 1rem;
      margin-bottom: 1.1rem;
    }

    .section-heading h2 {
      font-size: 1.9rem;
      letter-spacing: -0.02em;
    }

    .section-heading p, .subtle {
      margin: 0;
      color: var(--muted);
    }

    .collections {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(285px, 1fr));
      gap: 1rem;
    }

    .collection-card {
      display: flex;
      flex-direction: column;
      gap: 0.95rem;
      padding: 1.2rem 1.2rem 1.15rem;
      border-radius: 1.2rem;
      color: inherit;
      position: relative;
      overflow: hidden;
      transition: transform 140ms ease, border-color 140ms ease, background 140ms ease;
    }

    .collection-card::before {
      content: "";
      position: absolute;
      inset: 0 auto auto 0;
      width: 100%;
      height: 4px;
      background: linear-gradient(90deg, #8e3c27 0%, #b96845 100%);
      opacity: 0.95;
    }

    a.collection-card:hover {
      transform: translateY(-2px);
      border-color: rgba(122, 53, 32, 0.34);
      background: rgba(255, 250, 241, 0.99);
      text-decoration: none;
    }

    .collection-card.disabled {
      opacity: 0.76;
    }

    .card-header {
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 0.75rem;
    }

    .card-title {
      display: grid;
      gap: 0.22rem;
    }

    .card-title h3 {
      font-size: 1.2rem;
      letter-spacing: -0.01em;
    }

    .card-title p {
      margin: 0;
      color: var(--muted);
      font-size: 0.92rem;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      padding: 0.28rem 0.62rem;
      border-radius: 999px;
      border: 1px solid rgba(122, 53, 32, 0.18);
      background: rgba(122, 53, 32, 0.08);
      color: #6d2d1c;
      font-size: 0.76rem;
      font-weight: 700;
      white-space: nowrap;
    }

    .badge.scaffold {
      background: rgba(77, 60, 44, 0.07);
      color: var(--muted);
      border-color: rgba(77, 60, 44, 0.16);
    }

    .card-summary {
      margin: 0;
      min-height: 3.4em;
      color: #4e4740;
      font-size: 0.97rem;
    }

    .card-stats {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 0.55rem;
      padding-top: 0.95rem;
      border-top: 1px solid var(--line);
    }

    .card-stat {
      padding: 0.68rem 0.75rem;
      border-radius: 0.9rem;
      border: 1px solid rgba(77, 60, 44, 0.14);
      background: rgba(255, 255, 255, 0.66);
    }

    .card-stat strong {
      display: block;
      font-size: 1.12rem;
      line-height: 1.1;
    }

    .card-stat span {
      display: block;
      margin-top: 0.18rem;
      color: var(--muted);
      font-size: 0.82rem;
    }

    .note-panel {
      padding: 1.2rem 1.25rem;
      border-radius: 1.2rem;
    }

    .note-panel h2 {
      font-size: 1.18rem;
      margin-bottom: 0.2rem;
    }

    .note-panel p {
      margin: 0.35rem 0 0;
      color: #4e4740;
    }

    .footer {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      padding: 0.1rem 0.2rem 0;
      color: var(--muted);
      font-size: 0.92rem;
    }

    @media (max-width: 980px) {
      .hero {
        grid-template-columns: 1fr;
      }

      .section-heading {
        flex-direction: column;
        align-items: start;
      }
    }

    @media (max-width: 760px) {
      .page-shell {
        padding: 1rem;
      }

      .hero, .section-panel {
        padding: 1.2rem;
      }

      .hero-stats, .card-stats {
        grid-template-columns: 1fr 1fr;
      }

      .hero h1 {
        font-size: 2.15rem;
      }
    }

    @media (max-width: 560px) {
      .hero-stats, .card-stats, .collections {
        grid-template-columns: 1fr;
      }

      .badge {
        font-size: 0.88rem;
      }
    }
  </style>
</head>
<body>
  <div class="page-shell">
    <main class="hub">
      <section class="panel hero">
        <div>
          <a class="hero-brand" href="index.html">
            <img src="assets/paper_atlas_logo.svg" alt="">
            <span class="hero-brand-copy">
              <strong>{{ site_brand }}</strong>
              <span>research atlas</span>
            </span>
          </a>
          <p class="eyebrow">{{ site_brand }}</p>
          <h1>Research Collection Hub</h1>
          <p class="lede">
            Karpathy <code>LLM wiki</code> 패턴을 바탕으로 만든 연구용 지식 허브입니다.
            각 주제는 독립된 collection으로 관리되고, collection 안에서는 논문 PDF, source page, concept page, query, synthesis가 함께 연결됩니다.
          </p>
          <div class="hero-actions">
            {% if show_local_viewer_link %}
            <a class="hero-button" href="{{ local_viewer_href }}">Open Local Viewer</a>
            {% endif %}
          </div>
        </div>

        <div class="hero-stats">
          <article class="stat-card">
            <span class="stat-label">Collections</span>
            <strong>{{ totals.collections }}</strong>
          </article>
          <article class="stat-card">
            <span class="stat-label">Sources</span>
            <strong>{{ totals.sources }}</strong>
          </article>
          <article class="stat-card">
            <span class="stat-label">Concepts</span>
            <strong>{{ totals.concepts }}</strong>
          </article>
          <article class="stat-card">
            <span class="stat-label">Saved Analyses</span>
            <strong>{{ totals.saved_analyses }}</strong>
          </article>
        </div>
      </section>

      <section class="panel section-panel">
        <div class="section-heading">
          <div>
            <p class="eyebrow">Collections</p>
            <h2>Active Research Workspaces</h2>
          </div>
          <p class="subtle">
            {{ generated_at }} 기준으로 모든 collection 상태를 자동 집계합니다.
          </p>
        </div>

        <div class="collections">
          {% for collection in collections %}
          {% if collection.dashboard_exists %}
          <a class="collection-card" href="{{ collection.href }}" data-file-href="{{ collection.file_href }}" data-http-href="{{ collection.http_href }}">
          {% else %}
          <article class="collection-card disabled">
          {% endif %}
            <div class="card-header">
              <div class="card-title">
                <h3>{{ collection.title }}</h3>
                <p>{{ collection.subtitle }}</p>
              </div>
              <span class="badge {% if not collection.is_active %}scaffold{% endif %}">{{ collection.badge }}</span>
            </div>
            <p class="card-summary">{{ collection.summary }}</p>
            <div class="card-stats">
              <div class="card-stat">
                <strong>{{ collection.source_pages }}</strong>
                <span>sources</span>
              </div>
              <div class="card-stat">
                <strong>{{ collection.concept_pages }}</strong>
                <span>concepts</span>
              </div>
              <div class="card-stat">
                <strong>{{ collection.query_pages }}</strong>
                <span>queries</span>
              </div>
              <div class="card-stat">
                <strong>{{ collection.synthesis_pages }}</strong>
                <span>syntheses</span>
              </div>
            </div>
          {% if collection.dashboard_exists %}
          </a>
          {% else %}
          </article>
          {% endif %}
          {% endfor %}
        </div>
      </section>

      <section class="note-panel">
        <h2>How this stays in sync</h2>
        <p>
          각 collection HTML을 다시 렌더할 때 최상위 허브도 함께 재생성됩니다.
          루트 watcher를 사용하면 어떤 collection이 바뀌어도, 그리고 새 collection이 추가돼도 이 페이지가 자동으로 갱신됩니다.
        </p>
      </section>

      <footer class="footer">
        <span>Generated from collection metadata and current wiki counts.</span>
      </footer>
    </main>
  </div>
</body>
<script>
  (() => {
    let localViewerProbe = null;
    const isFileModeNavigation = () => window.location.protocol === "file:" || !/^https?:$/.test(window.location.protocol);
    const getLocalViewerOrigin = (httpHref) => {
      try {
        return new URL(httpHref).origin;
      } catch (_error) {
        return "";
      }
    };
    const canReachLocalViewer = (httpHref) => {
      const origin = getLocalViewerOrigin(httpHref);
      if (!origin) {
        return Promise.resolve(false);
      }
      if (localViewerProbe && localViewerProbe.origin === origin) {
        return localViewerProbe.promise;
      }
      localViewerProbe = {
        origin,
        promise: new Promise((resolve) => {
          const controller = typeof AbortController === "function" ? new AbortController() : null;
          const timeoutId = window.setTimeout(() => {
            if (controller) {
              controller.abort();
            }
            resolve(false);
          }, 450);
          fetch(`${origin}/__paper_collect_ping__`, {
            method: "GET",
            cache: "no-store",
            mode: "no-cors",
            signal: controller ? controller.signal : undefined,
          })
            .then(() => {
              window.clearTimeout(timeoutId);
              resolve(true);
            })
            .catch(() => {
              window.clearTimeout(timeoutId);
              resolve(false);
            });
        }),
      };
      return localViewerProbe.promise;
    };

    const preferredNavigationTarget = async (link) => {
      const fileHref = link.getAttribute("data-file-href");
      const httpHref = link.getAttribute("data-http-href");
      const href = link.getAttribute("href");
      if (!isFileModeNavigation()) {
        return href || httpHref || fileHref || "#";
      }
      if (httpHref && await canReachLocalViewer(httpHref)) {
        return httpHref;
      }
      return fileHref || href || httpHref || "#";
    };

    document.addEventListener("click", async (event) => {
      const link = event.target.closest ? event.target.closest("a[data-file-href], a[data-http-href]") : null;
      if (!link || !isFileModeNavigation()) {
        return;
      }
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
        return;
      }
      event.preventDefault();
      const target = await preferredNavigationTarget(link);
      if (target) {
        window.location.assign(target);
      }
    });
  })();
</script>
</html>
"""
)


def count_files(directory: Path, pattern: str = "*") -> int:
    if not directory.exists():
        return 0
    return sum(1 for path in directory.glob(pattern) if path.is_file())


def build_root_hub_context() -> Dict[str, object]:
    collections = []
    for workspace in list_collection_workspaces():
        source_pages = count_files(workspace.wiki_dir / "sources", "*.md")
        concept_pages = count_files(workspace.wiki_dir / "concepts", "*.md")
        query_pages = count_files(workspace.wiki_dir / "queries", "*.md")
        synthesis_pages = count_files(workspace.wiki_dir / "syntheses", "*.md")
        dashboard_exists = (workspace.wiki_html_dir / "index.html").exists()
        is_active = any((source_pages, concept_pages, query_pages, synthesis_pages))
        collections.append(
            {
                "key": workspace.key,
                "title": workspace.title,
                "subtitle": workspace.description,
                "summary": workspace.description,
                "href": f"collections/{workspace.key}/wiki_html/index.html",
                "file_href": (workspace.wiki_html_dir / "index.html").resolve().as_uri(),
                "http_href": http_href_for_path(workspace.wiki_html_dir / "index.html"),
                "dashboard_exists": dashboard_exists,
                "is_active": is_active,
                "badge": "Active" if is_active else "Scaffold",
                "source_pages": source_pages,
                "concept_pages": concept_pages,
                "query_pages": query_pages,
                "synthesis_pages": synthesis_pages,
            }
        )

    collections.sort(key=lambda item: (not item["is_active"], item["title"].lower()))
    totals = {
        "collections": len(collections),
        "sources": sum(item["source_pages"] for item in collections),
        "concepts": sum(item["concept_pages"] for item in collections),
        "saved_analyses": sum(item["query_pages"] + item["synthesis_pages"] for item in collections),
    }
    primary_collection = next((item for item in collections if item["dashboard_exists"]), None)
    generated_at = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    return {
        "collections": collections,
        "totals": totals,
        "primary_collection": primary_collection,
        "local_viewer_href": http_href_for_path(PROJECT_ROOT / "index.html"),
        "show_local_viewer_link": not PUBLIC_SITE_MODE,
        "generated_at": generated_at,
    }


def render_root_hub() -> Path:
    context = build_root_hub_context()
    output_path = PROJECT_ROOT / "index.html"
    output_path.write_text(ROOT_HUB_TEMPLATE.render(site_brand=SITE_BRAND, **context), encoding="utf-8")
    return output_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Render a collection wiki into a static HTML site."
    )
    parser.add_argument(
        "--collection",
        help="Collection name under collections/, for example longread-sequencing or organoid.",
    )
    parser.add_argument(
        "--workspace",
        help="Explicit workspace path. Overrides --collection.",
    )
    parser.add_argument(
        "--public-site",
        action="store_true",
        help="Render for public static hosting such as GitHub Pages.",
    )
    parser.add_argument(
        "--include-public-pdfs",
        action="store_true",
        help="When used with --public-site, keep raw PDF links in the rendered site.",
    )
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    configure_render_mode(
        public_site=args.public_site,
        include_pdfs=args.include_public_pdfs,
    )
    workspace = resolve_workspace(
        collection=args.collection,
        workspace=args.workspace,
        default_collection="longread-sequencing",
    )
    if workspace.root == PROJECT_ROOT and not (workspace.root / "wiki").exists():
        output_path = render_root_hub()
        print("Rendered collection hub to %s" % output_path)
        return
    configure_workspace(workspace.root, workspace.title, workspace.description)
    pages = [build_page(path) for path in discover_markdown_files()]
    render_site(pages)
    render_root_hub()
    print("Rendered %d pages to %s" % (len(pages), OUTPUT_DIR))
    print("Open %s" % (OUTPUT_DIR / "index.html"))


if __name__ == "__main__":
    main()
