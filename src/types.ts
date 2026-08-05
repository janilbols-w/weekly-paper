export interface CategoryPath {
  domain_id: string;
  domain: string;
  domain_zh: string;
  group_id: string;
  group: string;
  group_zh: string;
  leaf_id: string;
  leaf: string;
  leaf_zh: string;
}

export interface PaperRecord {
  id: string;
  title: string;
  abstract: string;
  url: string;
  pdf_url: string;
  published: string;
  updated: string;
  authors: string[];
  source: string;
  source_type: string;
  code_url: string;
  score: number;
  summary_en: string;
  summary_zh: string;
  primary_category: CategoryPath;
  keyword_evidence: string[];
}

export interface WeekRecord {
  week: string;
  start_date: string;
  end_date: string;
  paper_ids: string[];
  featured_ids: string[];
}

export interface TaxonomyLeaf { id: string; name: string; name_zh: string; keywords: string[]; }
export interface TaxonomyGroup { id: string; name: string; name_zh: string; leaves: TaxonomyLeaf[]; }
export interface TaxonomyDomain { id: string; name: string; name_zh: string; groups: TaxonomyGroup[]; }
export interface Taxonomy { version: number; domains: TaxonomyDomain[]; }

export interface StatsRecord {
  total_papers: number;
  total_weeks: number;
  featured_total: number;
  code_available: number;
  leaf_counts: Record<string, number>;
  domain_counts: Record<string, number>;
  week_counts: Record<string, number>;
}

