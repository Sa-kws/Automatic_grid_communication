export class Grid {
  ID: string;
  Type: 'Grid';
  NumberOfCols: number;
  NumberOfRows: number;
  GapSize: number;

  ElementList: GridElement[];
  ImageList: Image[];
  PageList: Page[];

  BackgroundColor: string;

  constructor(gridId, gridType, gridCol, gridRow, elemList, imageList, pageList) {
    this.ID = gridId;
    this.Type = gridType;
    this.NumberOfCols = Number(gridCol);
    this.NumberOfRows = Number(gridRow);
    this.ElementList = elemList;
    this.ImageList = imageList;
    this.PageList = pageList;
  }

}

export class FolderGoTo {
  GoTo: string;

  constructor(goto) {
    this.GoTo = goto;
  }
}

export class GridElement {
  ID: string;
  Type: 'empty' | 'button' | FolderGoTo;
  PartOfSpeech: string;
  VisibilityLevel: number;
  x: number;
  y: number;
  cols: number;
  rows: number;

  style: { id: string } | Style;

  ElementFormsList: ElementForm[];
  InteractionsList: Interaction[];

  dragAndResizeEnabled: boolean;

  constructor(elementId: string, elementType, elementPartOfSpeech: string,
              color: string, borderColor: string, visibilityLevel, elementsForms: ElementForm[], interactionList: Interaction[]) {

    this.ID = elementId;
    this.Type = elementType;
    this.PartOfSpeech = elementPartOfSpeech;
    this.style = new Style(color, borderColor, 'black');
    this.VisibilityLevel = visibilityLevel;
    this.ElementFormsList = elementsForms;
    this.InteractionsList = interactionList;
    this.y = 0;
    this.x = 0;
    this.rows = 1;
    this.cols = 1;
    this.dragAndResizeEnabled = true;
  }
}

export class Vignette {
  Label: string;
  ImagePath: any;
  Color: string;
  BorderColor: string;
}

export class Interaction {
  ID: string; // 'click' | 'longPress' | 'doubleClick';
  ActionList: Action[];
}

export class Action {
  ID: string;
  Options: string[];
}

export class Page {
  ID: string;
  Name: string;
  ElementIDsList: string[];
  NumberOfCols: number;
  NumberOfRows: number;
  GapSize: number;
  BackgroundColor: string
}

export class Dictionary {
  dictionary: { id: string, FR: string, EN: string }[]
}